package com.systemvigiasus.monitoramento.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;

import com.systemvigiasus.monitoramento.domain.Ovitrampa;
import com.systemvigiasus.monitoramento.dto.OvitrampaRequestDTO;
import com.systemvigiasus.monitoramento.dto.OvitrampaResponseDTO;
import com.systemvigiasus.monitoramento.repository.OvitrampaRepository;

@Service
public class OvitrampaService {

    private final OvitrampaRepository ovitrampaRepository;

    public OvitrampaService(OvitrampaRepository ovitrampaRepository) {
        this.ovitrampaRepository = ovitrampaRepository;
    }

    public OvitrampaResponseDTO cadastrarOvitrampa(OvitrampaRequestDTO request) {
        Ovitrampa ovitrampa = new Ovitrampa(
                null,
                normalizarCodigoArea(request.getCodigoArea()),
                request.getBairro(),
                request.getTotalArmadilhas(),
                request.getTotalNegativas(),
                request.getPercentualNegativas(),
                request.getTotalPositivas(),
                request.getPercentualPositivas()
        );

        Ovitrampa ovitrampaSalva = ovitrampaRepository.save(ovitrampa);
        return converterParaResponse(ovitrampaSalva);
    }

    public List<OvitrampaResponseDTO> listarOvitrampas() {
        return ovitrampaRepository.findAll()
                .stream()
                .map(this::converterParaResponse)
                .collect(Collectors.toList());
    }

    public OvitrampaResponseDTO buscarPorId(Long id) {
        return ovitrampaRepository.findById(id)
                .map(this::converterParaResponse)
                .orElse(null);
    }

    public List<OvitrampaResponseDTO> buscarPorCodigoArea(String codigoArea) {
        String codigoNormalizado = normalizarCodigoArea(codigoArea);

        return ovitrampaRepository.findByCodigoArea(codigoNormalizado)
                .stream()
                .map(this::converterParaResponse)
                .collect(Collectors.toList());
    }

    private OvitrampaResponseDTO converterParaResponse(Ovitrampa ovitrampa) {
        return new OvitrampaResponseDTO(
                ovitrampa.getId(),
                ovitrampa.getCodigoArea(),
                ovitrampa.getBairro(),
                ovitrampa.getTotalArmadilhas(),
                ovitrampa.getTotalNegativas(),
                ovitrampa.getPercentualNegativas(),
                ovitrampa.getTotalPositivas(),
                ovitrampa.getPercentualPositivas()
        );
    }

    private String normalizarCodigoArea(String codigoArea) {
        if (codigoArea == null) {
            return null;
        }

        String codigoLimpo = codigoArea.trim();

        if (codigoLimpo.matches("\\d+")) {
            return String.format("%03d", Integer.parseInt(codigoLimpo));
        }

        return codigoLimpo;
    }
}