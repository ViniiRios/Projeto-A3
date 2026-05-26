package com.systemvigiasus.monitoramento.ui;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.systemvigiasus.monitoramento.dto.AreaCadastroRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaCadastroResponseDTO;
import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.service.AreaCadastroService;
import com.systemvigiasus.monitoramento.service.EpidemiologiaService;

@RestController
@RequestMapping("/api/areas")
public class AreaController {

    @Autowired
    private EpidemiologiaService epidemiologiaService;

    @Autowired
    private AreaCadastroService areaCadastroService;

    @PostMapping("/calcular-risco")
    public ResponseEntity<AreaResponseDTO> calcularRisco(@RequestBody AreaRequestDTO request) {
        AreaResponseDTO response = epidemiologiaService.calcularRiscoArea(request);
        return ResponseEntity.ok(response);
    }

    @PostMapping
    public ResponseEntity<AreaCadastroResponseDTO> cadastrarArea(@RequestBody AreaCadastroRequestDTO request) {
        AreaCadastroResponseDTO response = areaCadastroService.cadastrarArea(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @GetMapping
    public ResponseEntity<List<AreaCadastroResponseDTO>> listarAreas() {
        List<AreaCadastroResponseDTO> response = areaCadastroService.listarAreas();
        return ResponseEntity.ok(response);
    }

    @GetMapping("/{id}")
    public ResponseEntity<AreaCadastroResponseDTO> buscarAreaPorId(@PathVariable Long id) {
        AreaCadastroResponseDTO response = areaCadastroService.buscarPorId(id);

        if (response == null) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.ok(response);
    }
}