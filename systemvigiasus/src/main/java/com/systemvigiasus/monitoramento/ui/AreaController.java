package com.systemvigiasus.monitoramento.ui;

import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.service.AreaService;
import com.systemvigiasus.monitoramento.service.EpidemiologiaService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/areas")
public class AreaController {

    @Autowired
    private AreaService areaService;

    @PostMapping("/calcular-risco")
    public ResponseEntity<AreaResponseDTO> calcularRisco(@RequestBody AreaRequestDTO request) {
        AreaResponseDTO response = areaService.obterDetalhesDaArea(request);
        return ResponseEntity.ok(response);
    }
}