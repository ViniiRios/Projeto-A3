package com.systemvigiasus.monitoramento.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import static org.mockito.ArgumentMatchers.any;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import static org.mockito.Mockito.when;
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
        request.setId(1L);
        request.setNome("Área de Teste");
        request.setNumeroCasos(100);
        request.setCasosLag2(80);
        request.setTemperatura(25.0);
        request.setChuva(150.0);
        request.setPopulacao(1000);
        request.setMes(6);
        request.setAno(2026);

        IAPredictionResponse mockIA = new IAPredictionResponse(
                200.0,      // taxaIncidencia
                10000.0,    // taxaAtual
                200.0,      // taxaPrevistaModelo
                2.0,        // casosPrevistosModelo
                200.0,      // indiceRiscoConsiderado
                "ALTO",     // risco
                "RED",      // corAlerta
                "SUCCESS"   // status
        );

        when(iaService.obterPrevisaoDaIA(any())).thenReturn(mockIA);

        AreaResponseDTO response = service.calcularRiscoArea(request);

        assertNotNull(response);
        assertEquals("ALTO", response.getRisco());
        assertEquals(200.0, response.getTaxaIncidencia());
        assertEquals(10000.0, response.getTaxaAtual());
        assertEquals(200.0, response.getTaxaPrevistaModelo());
        assertEquals(2.0, response.getCasosPrevistosModelo());
        assertEquals(200.0, response.getIndiceRiscoConsiderado());
        assertTrue(response.getTaxaAtual() > 50);
    }
}