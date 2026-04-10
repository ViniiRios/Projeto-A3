package com.systemvigiasus.monitoramento.service;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.dto.IAPredictionRequest;
import com.systemvigiasus.monitoramento.dto.IAPredictionResponse;
import java.time.LocalDate;

@Service
public class EpidemiologiaService {

    @Autowired
    private IAIntegrationService iaService;

    public AreaResponseDTO calcularRiscoArea(AreaRequestDTO request) {
        double taxaIncidencia = (double) request.getNumeroCasos() / request.getPopulacao() * 100000;

        IAPredictionRequest iaRequest = new IAPredictionRequest(
            request.getMes(),             
            request.getAno(),             
            request.getNumeroCasos(),      
            request.getCasosLag2(),       
            request.getTemperatura(),      
            request.getTemperatura() - 2, 
            request.getChuva(),           
            request.getChuva() - 50,
            1012.0,
            1011.0
        );

        IAPredictionResponse previsao = iaService.obterPrevisaoDaIA(iaRequest);

        return new AreaResponseDTO(
            request.getId(),
            request.getNome(),
            previsao.nivel_risco(),
            taxaIncidencia
        );
    }
}