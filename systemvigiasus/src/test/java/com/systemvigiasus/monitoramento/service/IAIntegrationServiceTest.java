package com.systemvigiasus.monitoramento.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.mockito.junit.jupiter.MockitoSettings;
import org.mockito.quality.Strictness;
import org.springframework.web.client.RestTemplate;
import org.junit.jupiter.api.DisplayName;

import com.systemvigiasus.monitoramento.dto.IAPredictionRequest;
import com.systemvigiasus.monitoramento.dto.IAPredictionResponse;

@ExtendWith(MockitoExtension.class)
@MockitoSettings(strictness = Strictness.LENIENT)
class IAIntegrationServiceTest {

    @Mock
    private RestTemplate restTemplate;

    @InjectMocks
    private IAIntegrationService iaIntegrationService;

    @Test
    @DisplayName("Deve tratar falha de conexão com o Python")
    void deveRetornarServicoIndisponivelQuandoPythonFalhar() {

        IAPredictionRequest request = new IAPredictionRequest(4, 2026, 400, 250, 28.0, 26.0, 100.0, 50.0, 1012.0, 1011.0, 200000);
        
        when(restTemplate.postForObject(any(String.class), any(IAPredictionRequest.class), eq(IAPredictionResponse.class)))
            .thenThrow(new RuntimeException("Conexão Recusada"));

        IAPredictionResponse response = iaIntegrationService.obterPrevisaoDaIA(request);

        assertEquals("RISCO MODERADO", response.risco()); 
        assertEquals("ORANGE", response.corAlerta());
    }
}