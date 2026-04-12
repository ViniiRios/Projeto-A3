package com.systemvigiasus.monitoramento.dto;

public class RiscoResponseDTO {
    private String risco;
    private Double taxaIncidencia;

    public RiscoResponseDTO() {
    }

    public RiscoResponseDTO(String risco, Double taxaIncidencia) {
        this.risco = risco;
        this.taxaIncidencia = taxaIncidencia;
    }

    public String getRisco() {
        return risco;
    }

    public void setRisco(String risco) {
        this.risco = risco;
    }

    public Double getTaxaIncidencia() {
        return taxaIncidencia;
    }

    public void setTaxaIncidencia(Double taxaIncidencia) {
        this.taxaIncidencia = taxaIncidencia;
    }
}