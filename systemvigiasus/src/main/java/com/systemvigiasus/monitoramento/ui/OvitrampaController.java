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

import com.systemvigiasus.monitoramento.dto.OvitrampaRequestDTO;
import com.systemvigiasus.monitoramento.dto.OvitrampaResponseDTO;
import com.systemvigiasus.monitoramento.service.OvitrampaService;

@RestController
@RequestMapping("/api/ovitrampas")
public class OvitrampaController {

    private final OvitrampaService ovitrampaService;

    public OvitrampaController(OvitrampaService ovitrampaService) {
        this.ovitrampaService = ovitrampaService;
    }

    @PostMapping
    public ResponseEntity<OvitrampaResponseDTO> cadastrarOvitrampa(@RequestBody OvitrampaRequestDTO request) {
        OvitrampaResponseDTO response = ovitrampaService.cadastrarOvitrampa(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @GetMapping
    public ResponseEntity<List<OvitrampaResponseDTO>> listarOvitrampas() {
        List<OvitrampaResponseDTO> response = ovitrampaService.listarOvitrampas();
        return ResponseEntity.ok(response);
    }

    @GetMapping("/{id}")
    public ResponseEntity<OvitrampaResponseDTO> buscarOvitrampaPorId(@PathVariable Long id) {
        OvitrampaResponseDTO response = ovitrampaService.buscarPorId(id);

        if (response == null) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.ok(response);
    }

    @GetMapping("/area/{codigoArea}")
    public ResponseEntity<List<OvitrampaResponseDTO>> buscarOvitrampasPorCodigoArea(@PathVariable String codigoArea) {
        List<OvitrampaResponseDTO> response = ovitrampaService.buscarPorCodigoArea(codigoArea);
        return ResponseEntity.ok(response);
    }
}