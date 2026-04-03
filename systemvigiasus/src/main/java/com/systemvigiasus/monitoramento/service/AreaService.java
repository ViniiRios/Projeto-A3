package com.systemvigiasus.monitoramento.service;

import org.springframework.stereotype.Service;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;

@Service
public class AreaService {

    public AreaResponseDTO calcularRiscoEpidemiologico(AreaRequestDTO dados) {
        double percentualPositivas = (double) dados.getPositivas() / dados.getTotalArmadilhas() * 100;
        
        String nivelRisco;
        
        if (percentualPositivas > 50) {
            nivelRisco = "ALTO";
        } else if (percentualPositivas >= 20) {
            nivelRisco = "MÉDIO";
        } else {
            nivelRisco = "BAIXO";
        }

        AreaResponseDTO resposta = new AreaResponseDTO();
        resposta.setNome(dados.getNome());
        resposta.setRisco(nivelRisco);
        
        return resposta;
    }
}