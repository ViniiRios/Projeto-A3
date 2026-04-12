package com.systemvigiasus.monitoramento.client;

import com.systemvigiasus.monitoramento.client.IAClient;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.RiscoResponseDTO;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
public class IAClient {

    private final String IA_URL = "http://localhost:5000/predict";

    public RiscoResponseDTO chamarMotorIA(AreaRequestDTO dados) {
        RestTemplate restTemplate = new RestTemplate();
        
        try {
            return restTemplate.postForObject(IA_URL, dados, RiscoResponseDTO.class);
        } catch (Exception e) {
            System.err.println("Erro ao conectar com o Motor de IA: " + e.getMessage());
            return new RiscoResponseDTO("ERRO_CONEXAO", 0.0);
        }
    }
}