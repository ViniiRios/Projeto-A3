package com.systemvigiasus.monitoramento.service; 

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.dto.IAPredictionResponse;

@ExtendWith(MockitoExtension.class)
class EpidemiologiaServiceTest {

    @Mock
    private IAIntegrationService iaService;

    @InjectMocks
    private EpidemiologiaService service;

    @Test
    void deveCalcularRiscoAltoQuandoIncidenciaForElevada() {
        AreaRequestDTO request = new AreaRequestDTO();
        request.setNumeroCasos(100);
        request.setPopulacao(1000);

        IAPredictionResponse mockIA = new IAPredictionResponse(200.0, "ALTO", "RED", "SUCCESS");
        when(iaService.obterPrevisaoDaIA(any())).thenReturn(mockIA);

        AreaResponseDTO response = service.calcularRiscoArea(request);

        assertEquals("ALTO", response.getRisco()); 
        assertTrue(response.getTaxaIncidencia() > 50);
        assertNotNull(response.getRisco());
    }
}