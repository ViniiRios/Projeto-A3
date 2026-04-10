package com.systemvigiasus.monitoramento.dto;

public record IAPredictionResponse(
    int casos_previstos,
    String nivel_risco,
    String cor_alerta,
    String status
) {}