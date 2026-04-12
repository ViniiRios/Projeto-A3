package com.systemvigiasus.monitoramento.service;

import com.systemvigiasus.monitoramento.client.IAClient;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.dto.RiscoResponseDTO;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)

public class AreaServiceTest {

    @InjectMocks
    private AreaService areaService; 

    @Mock
    private IAClient iaClient; 

    @Test
    void deveRetornarRiscoAltoQuandoCondicoesFavoraveis() {
        AreaRequestDTO request = new AreaRequestDTO(31.5, 180.0, 450); 
        RiscoResponseDTO respostaIA = new RiscoResponseDTO("ALERTA MÁXIMO", 2800.0);
        
        when(iaClient.chamarMotorIA(any())).thenReturn(respostaIA);

        AreaResponseDTO resultado = areaService.processarPredicao(request);

        assertNotNull(resultado);
        assertEquals("ALERTA MÁXIMO", resultado.getRisco());
        assertTrue(resultado.getTaxaIncidencia() > 2000);
        verify(iaClient, times(1)).chamarMotorIA(any());
    }
}