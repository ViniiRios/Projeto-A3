package com.systemvigiasus.monitoramento.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import com.systemvigiasus.monitoramento.client.IAClient;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.dto.RiscoResponseDTO;

@ExtendWith(MockitoExtension.class)
class AreaServiceTest {

    @Mock
    private IAClient iaClient;

    @InjectMocks
    private AreaService areaService;

    @Test
    void deveProcessarPredicaoComSucesso() {
        AreaRequestDTO request = new AreaRequestDTO();
        RiscoResponseDTO mockRisco = new RiscoResponseDTO("RISCO BAIXO", 10.5);
        
        when(iaClient.chamarMotorIA(any())).thenReturn(mockRisco);

        AreaResponseDTO resultado = areaService.processarPredicao(request);

        assertEquals("RISCO BAIXO", resultado.getRisco());
        assertEquals(10.5, resultado.getTaxaIncidencia());
        verify(iaClient).chamarMotorIA(request);
    }
}