package com.systemvigiasus.monitoramento.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;

import com.systemvigiasus.monitoramento.domain.CasoClima;
import com.systemvigiasus.monitoramento.dto.CasoClimaRequestDTO;
import com.systemvigiasus.monitoramento.dto.CasoClimaResponseDTO;
import com.systemvigiasus.monitoramento.repository.CasoClimaRepository;

@Service
public class CasoClimaService {

    private final CasoClimaRepository casoClimaRepository;

    public CasoClimaService(CasoClimaRepository casoClimaRepository) {
        this.casoClimaRepository = casoClimaRepository;
    }

    public CasoClimaResponseDTO cadastrarCasoClima(CasoClimaRequestDTO request) {
        CasoClima casoClima = new CasoClima(
                null,
                request.getPeriodoReferencia(),
                request.getRegional(),
                request.getCasosDengue(),
                request.getCasosChikungunya(),
                request.getCasosZika(),
                request.getCasosTotal(),
                request.getTemperaturaMedia(),
                request.getPrecipitacaoTotal(),
                request.getPopulacaoRegional()
        );

        CasoClima casoClimaSalvo = casoClimaRepository.save(casoClima);
        return converterParaResponse(casoClimaSalvo);
    }

    public List<CasoClimaResponseDTO> listarCasosClima() {
        return casoClimaRepository.findAll()
                .stream()
                .map(this::converterParaResponse)
                .collect(Collectors.toList());
    }

    public CasoClimaResponseDTO buscarPorId(Long id) {
        return casoClimaRepository.findById(id)
                .map(this::converterParaResponse)
                .orElse(null);
    }

    private CasoClimaResponseDTO converterParaResponse(CasoClima casoClima) {
        return new CasoClimaResponseDTO(
                casoClima.getId(),
                casoClima.getPeriodoReferencia(),
                casoClima.getRegional(),
                casoClima.getCasosDengue(),
                casoClima.getCasosChikungunya(),
                casoClima.getCasosZika(),
                casoClima.getCasosTotal(),
                casoClima.getTemperaturaMedia(),
                casoClima.getPrecipitacaoTotal(),
                casoClima.getPopulacaoRegional()
        );
    }
}