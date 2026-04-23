package com.systemvigiasus.monitoramento.ui;

import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.service.EpidemiologiaService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/areas")
public class AreaController {

    @Autowired
    private EpidemiologiaService epidemiologiaService;

    @PostMapping("/calcular-risco")
    public AreaResponseDTO calcular(@RequestBody AreaRequestDTO request) {
        return epidemiologiaService.calcularRiscoArea(request); 
    }
}