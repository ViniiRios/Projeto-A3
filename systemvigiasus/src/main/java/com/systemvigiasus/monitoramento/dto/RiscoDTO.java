package com.systemvigiasus.monitoramento.dto;

public class RiscoDTO {
    private String nivel; 
    private Double valor;

    public RiscoDTO() {}

    public RiscoDTO(String nivel, Double valor) {
        this.nivel = nivel;
        this.valor = valor;
    }

    public String getNivel() { return nivel; }
    public void setNivel(String nivel) { this.nivel = nivel; }

    public Double getValor() { return valor; }
    public void setValor(Double valor) { this.valor = valor; }
}