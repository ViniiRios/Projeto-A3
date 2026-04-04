package com.systemvigiasus.monitoramento.service;

import org.springframework.stereotype.Service;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;

@Service
public class AreaService {

    public AreaResponseDTO calcularRiscoEpidemiologico(AreaRequestDTO dados) {
        double taxaIncidencia = (double) dados.getNumeroCasos() / dados.getPopulacao() * 100000;
        
        String nivelRisco;
        
        if (taxaIncidencia > 50) {
            nivelRisco = "ALTO";
        } else if (taxaIncidencia >= 20) {
            nivelRisco = "MÉDIO";
        } else {
            nivelRisco = "BAIXO";
        }

        AreaResponseDTO resposta = new AreaResponseDTO();
        resposta.setNome(dados.getNome());
        resposta.setRisco(nivelRisco);
        resposta.setTaxaIncidencia(taxaIncidencia);
        return resposta;
    }
}