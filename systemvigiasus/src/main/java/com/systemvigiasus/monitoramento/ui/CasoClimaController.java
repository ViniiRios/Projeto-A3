package com.systemvigiasus.monitoramento.ui;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.systemvigiasus.monitoramento.dto.CasoClimaRequestDTO;
import com.systemvigiasus.monitoramento.dto.CasoClimaResponseDTO;
import com.systemvigiasus.monitoramento.service.CasoClimaService;

@RestController
@RequestMapping("/api/casos-clima")
public class CasoClimaController {

    private final CasoClimaService casoClimaService;

    public CasoClimaController(CasoClimaService casoClimaService) {
        this.casoClimaService = casoClimaService;
    }

    @PostMapping
    public ResponseEntity<CasoClimaResponseDTO> cadastrarCasoClima(@RequestBody CasoClimaRequestDTO request) {
        CasoClimaResponseDTO response = casoClimaService.cadastrarCasoClima(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @GetMapping
    public ResponseEntity<List<CasoClimaResponseDTO>> listarCasosClima() {
        List<CasoClimaResponseDTO> response = casoClimaService.listarCasosClima();
        return ResponseEntity.ok(response);
    }

    @GetMapping("/{id}")
    public ResponseEntity<CasoClimaResponseDTO> buscarCasoClimaPorId(@PathVariable Long id) {
        CasoClimaResponseDTO response = casoClimaService.buscarPorId(id);

        if (response == null) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.ok(response);
    }
}