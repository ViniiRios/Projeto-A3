package com.systemvigiasus.monitoramento.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

import org.springframework.stereotype.Service;

import com.systemvigiasus.monitoramento.domain.Area;
import com.systemvigiasus.monitoramento.dto.AreaCadastroRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaCadastroResponseDTO;

@Service
public class AreaCadastroService {

    private final Map<Long, Area> areas = new HashMap<>();
    private final AtomicLong contadorId = new AtomicLong(1);

    public AreaCadastroResponseDTO cadastrarArea(AreaCadastroRequestDTO request) {
        Long id = contadorId.getAndIncrement();

        Area area = new Area(
                id,
                request.getNome(),
                request.getUnidadeSaude(),
                request.getBairro(),
                request.getRegionalOuDistrito(),
                request.getPopulacaoReferencia(),
                request.getStatus()
        );

        areas.put(id, area);

        return converterParaResponse(area);
    }

    public List<AreaCadastroResponseDTO> listarAreas() {
        List<AreaCadastroResponseDTO> resposta = new ArrayList<>();

        for (Area area : areas.values()) {
            resposta.add(converterParaResponse(area));
        }

        return resposta;
    }

    public AreaCadastroResponseDTO buscarPorId(Long id) {
        Area area = areas.get(id);

        if (area == null) {
            return null;
        }

        return converterParaResponse(area);
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