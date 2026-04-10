package com.systemvigiasus.monitoramento.service;

import org.springframework.stereotype.Service;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;

@Service
public class EpidemiologiaService {

    public AreaResponseDTO calcularRiscoArea(AreaRequestDTO request) {
        double taxaIncidencia = (double) request.getNumeroCasos() / request.getPopulacao() * 100000;
        
        String nivelRisco;
        if (taxaIncidencia > 50) {
            nivelRisco = "ALTO";
        } else if (taxaIncidencia > 20) {
            nivelRisco = "MODERADO";
        } else {
            nivelRisco = "BAIXO";
        }

        return new AreaResponseDTO(
            request.getId(),    
            request.getNome(),
            nivelRisco,
            taxaIncidencia
        );
    }
}