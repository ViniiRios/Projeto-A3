package com.systemvigiasus.monitoramento.service; 

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.junit.jupiter.MockitoExtension;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;

@ExtendWith(MockitoExtension.class)
class EpidemiologiaServiceTest {

    @InjectMocks
    private EpidemiologiaService service;

    @Test
    void deveCalcularRiscoAltoQuandoIncidenciaForElevada() {
        AreaRequestDTO request = new AreaRequestDTO();
        request.setNumeroCasos(100);
        request.setPopulacao(1000);

        AreaResponseDTO response = service.calcularRiscoArea(request);

        assertEquals("ALTO", response.getRisco()); 
        assertTrue(response.getTaxaIncidencia() > 50);
        assertNotNull(response.getRisco());
    }
}