package com.systemvigiasus.monitoramento.dto;

public class AreaResponseDTO {

    private Long id;
    private String nome;
    private String risco;
    private double taxaIncidencia;

    public AreaResponseDTO() {}

    public AreaResponseDTO(Long id, String nome, String risco, double taxaIncidencia) {
        this.id = id;
        this.nome = nome;
        this.risco = risco;
        this.taxaIncidencia = taxaIncidencia;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getRisco() { return risco; }
    public void setRisco(String risco) { this.risco = risco; }

    public double getTaxaIncidencia() { return taxaIncidencia; }
    public void setTaxaIncidencia(double taxaIncidencia) { this.taxaIncidencia = taxaIncidencia; }
}