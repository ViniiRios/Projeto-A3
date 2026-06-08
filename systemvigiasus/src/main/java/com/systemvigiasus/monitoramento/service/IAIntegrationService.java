package com.systemvigiasus.monitoramento.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.systemvigiasus.monitoramento.dto.IAPredictionRequest;
import com.systemvigiasus.monitoramento.dto.IAPredictionResponse;

@Service
public class IAIntegrationService {

    private final String PYTHON_URL = "http://localhost:5000/predict";

    private final RestTemplate restTemplate = new RestTemplate();

    public IAPredictionResponse obterPrevisaoDaIA(IAPredictionRequest request) {
        try {
            return restTemplate.postForObject(PYTHON_URL, request, IAPredictionResponse.class);
        } catch (Exception e) {
            System.err.println("Erro ao conectar com a IA: " + e.getMessage());

            return new IAPredictionResponse(
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    "SERVIÇO INDISPONÍVEL",
                    "GRAY",
                    "Erro de conexão"
            );
        }
    }
}