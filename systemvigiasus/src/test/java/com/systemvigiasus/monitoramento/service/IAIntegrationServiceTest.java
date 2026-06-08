package com.systemvigiasus.monitoramento.service;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import org.junit.jupiter.api.Test;

import com.systemvigiasus.monitoramento.dto.IAPredictionRequest;
import com.systemvigiasus.monitoramento.dto.IAPredictionResponse;

class IAIntegrationServiceTest {

    @Test
    void deveRetornarRespostaValidaDaIntegracaoComIA() {
        IAIntegrationService service = new IAIntegrationService();

        IAPredictionRequest request = new IAPredictionRequest(
                6,
                2026,
                500,
                300,
                25.0,
                23.0,
                150.0,
                100.0,
                900.0,
                900.5,
                2500000
        );

        IAPredictionResponse response = service.obterPrevisaoDaIA(request);

        assertNotNull(response);
        assertNotNull(response.risco());
        assertNotNull(response.corAlerta());
        assertNotNull(response.status());
    }
}