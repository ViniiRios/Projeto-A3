package com.systemvigiasus.monitoramento.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public record IAPredictionResponse(
    double taxaIncidencia,
    double taxaAtual,
    double taxaPrevistaModelo,
    double casosPrevistosModelo,
    double indiceRiscoConsiderado,
    String risco,
    String corAlerta,
    String status
) {}