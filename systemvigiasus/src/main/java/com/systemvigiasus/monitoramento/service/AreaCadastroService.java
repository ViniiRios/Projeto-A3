package com.systemvigiasus.monitoramento.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;

import com.systemvigiasus.monitoramento.domain.Area;
import com.systemvigiasus.monitoramento.dto.AreaCadastroRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaCadastroResponseDTO;
import com.systemvigiasus.monitoramento.repository.AreaRepository;

@Service
public class AreaCadastroService {

    private final AreaRepository areaRepository;

    public AreaCadastroService(AreaRepository areaRepository) {
        this.areaRepository = areaRepository;
    }

    public AreaCadastroResponseDTO cadastrarArea(AreaCadastroRequestDTO request) {
        String codigoAreaGerado = gerarProximoCodigoArea();

        Area area = new Area(
                null,
                codigoAreaGerado,
                request.getNome(),
                request.getUnidadeSaude(),
                request.getBairro(),
                request.getRegionalOuDistrito(),
                request.getPopulacaoReferencia(),
                "ATIVA"
        );

        Area areaSalva = areaRepository.save(area);
        return converterParaResponse(areaSalva);
    }

    public List<AreaCadastroResponseDTO> listarAreas() {
        return areaRepository.findAll()
                .stream()
                .map(this::converterParaResponse)
                .collect(Collectors.toList());
    }

    public AreaCadastroResponseDTO buscarPorId(Long id) {
        return areaRepository.findById(id)
                .map(this::converterParaResponse)
                .orElse(null);
    }

    public AreaCadastroResponseDTO inativarArea(Long id) {
        return areaRepository.findById(id)
                .map(area -> {
                    area.setStatus("INATIVA");
                    Area areaSalva = areaRepository.save(area);
                    return converterParaResponse(areaSalva);
                })
                .orElse(null);
    }

    public AreaCadastroResponseDTO reativarArea(Long id) {
        return areaRepository.findById(id)
                .map(area -> {
                    area.setStatus("ATIVA");
                    Area areaSalva = areaRepository.save(area);
                    return converterParaResponse(areaSalva);
                })
                .orElse(null);
    }

    private String gerarProximoCodigoArea() {
        int maiorCodigo = areaRepository.findAll()
                .stream()
                .map(Area::getCodigoArea)
                .filter(codigo -> codigo != null && codigo.trim().matches("\\d+"))
                .map(String::trim)
                .mapToInt(Integer::parseInt)
                .max()
                .orElse(-1);

        return String.format("%03d", maiorCodigo + 1);
    }

    private AreaCadastroResponseDTO converterParaResponse(Area area) {
        return new AreaCadastroResponseDTO(
                area.getId(),
                area.getCodigoArea(),
                area.getNome(),
                area.getUnidadeSaude(),
                area.getBairro(),
                area.getRegionalOuDistrito(),
                area.getPopulacaoReferencia(),
                area.getStatus()
        );
    }
}