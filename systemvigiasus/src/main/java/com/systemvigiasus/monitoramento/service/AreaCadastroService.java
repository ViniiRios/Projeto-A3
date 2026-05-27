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
        Area area = new Area(
                null,
                request.getNome(),
                request.getUnidadeSaude(),
                request.getBairro(),
                request.getRegionalOuDistrito(),
                request.getPopulacaoReferencia(),
                request.getStatus()
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

    private AreaCadastroResponseDTO converterParaResponse(Area area) {
        return new AreaCadastroResponseDTO(
                area.getId(),
                area.getNome(),
                area.getUnidadeSaude(),
                area.getBairro(),
                area.getRegionalOuDistrito(),
                area.getPopulacaoReferencia(),
                area.getStatus()
        );
    }
}