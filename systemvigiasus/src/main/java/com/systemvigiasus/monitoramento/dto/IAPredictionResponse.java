package com.systemvigiasus.monitoramento.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public record IAPredictionResponse(
    double taxaIncidencia,
    String risco,
    String corAlerta,
    String status
) {}