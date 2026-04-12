package com.systemvigiasus.monitoramento.service;

import com.systemvigiasus.monitoramento.client.IAClient;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.dto.RiscoResponseDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AreaService {

    @Autowired
    private IAClient iaClient;

    public AreaResponseDTO processarPredicao(AreaRequestDTO request) {
        RiscoResponseDTO respostaIA = iaClient.chamarMotorIA(request);
        return new AreaResponseDTO(respostaIA.getRisco(), respostaIA.getTaxaIncidencia());
    }

    public AreaResponseDTO obterDetalhesDaArea(AreaRequestDTO request) {
        return processarPredicao(request);
    }
}