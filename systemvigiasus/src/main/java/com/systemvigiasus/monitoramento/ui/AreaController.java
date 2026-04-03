package com.systemvigiasus.monitoramento.ui;

import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.service.AreaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/areas")
public class AreaController {

    @PostMapping("/calcular-risco")
    public AreaResponseDTO calcularRisco(@RequestBody AreaRequestDTO request) {
        return areaService.calcularRiscoEpidemiologico(request);
    }
}