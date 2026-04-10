package com.systemvigiasus.monitoramento.service;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;

@Service
public class AreaService {

    @Autowired
    private EpidemiologiaService epidemiologiaService;

    public AreaResponseDTO obterDetalhesDaArea(AreaRequestDTO dados) {
        return epidemiologiaService.calcularRiscoArea(dados);
    }
}