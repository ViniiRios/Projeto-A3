package com.systemvigiasus.monitoramento.dto;

public record IAPredictionRequest(
    int mes,
    int ano,
    int casos_lag1,
    int casos_lag2,
    double TEMP_MEDIA_lag1,
    double TEMP_MEDIA_lag2,
    double PRECIPITACAO_lag1,
    double PRECIPITACAO_lag2,
    double PRESSAO_MEDIA_lag1,
    double PRESSAO_MEDIA_lag2
) {}