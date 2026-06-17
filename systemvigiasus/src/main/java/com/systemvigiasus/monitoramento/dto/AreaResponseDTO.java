package com.systemvigiasus.monitoramento.dto;

public class AreaResponseDTO {

    private Long id;
    private String nome;
    private String risco;

    private double taxaIncidencia;
    private double taxaAtual;
    private double taxaPrevistaModelo;
    private double casosPrevistosModelo;
    private double indiceRiscoConsiderado;

    public AreaResponseDTO() {
    }

    public AreaResponseDTO(String risco, double taxaIncidencia) {
        this.risco = risco;
        this.taxaIncidencia = taxaIncidencia;
        this.indiceRiscoConsiderado = taxaIncidencia;
    }

    public AreaResponseDTO(Long id, String nome, String risco, double taxaIncidencia) {
        this.id = id;
        this.nome = nome;
        this.risco = risco;
        this.taxaIncidencia = taxaIncidencia;
        this.indiceRiscoConsiderado = taxaIncidencia;
    }

    public AreaResponseDTO(
            Long id,
            String nome,
            String risco,
            double taxaIncidencia,
            double taxaAtual,
            double taxaPrevistaModelo,
            double casosPrevistosModelo,
            double indiceRiscoConsiderado
    ) {
        this.id = id;
        this.nome = nome;
        this.risco = risco;
        this.taxaIncidencia = taxaIncidencia;
        this.taxaAtual = taxaAtual;
        this.taxaPrevistaModelo = taxaPrevistaModelo;
        this.casosPrevistosModelo = casosPrevistosModelo;
        this.indiceRiscoConsiderado = indiceRiscoConsiderado;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getRisco() {
        return risco;
    }

    public void setRisco(String risco) {
        this.risco = risco;
    }

    public double getTaxaIncidencia() {
        return taxaIncidencia;
    }

    public void setTaxaIncidencia(double taxaIncidencia) {
        this.taxaIncidencia = taxaIncidencia;
    }

    public double getTaxaAtual() {
        return taxaAtual;
    }

    public void setTaxaAtual(double taxaAtual) {
        this.taxaAtual = taxaAtual;
    }

    public double getTaxaPrevistaModelo() {
        return taxaPrevistaModelo;
    }

    public void setTaxaPrevistaModelo(double taxaPrevistaModelo) {
        this.taxaPrevistaModelo = taxaPrevistaModelo;
    }

    public double getCasosPrevistosModelo() {
        return casosPrevistosModelo;
    }

    public void setCasosPrevistosModelo(double casosPrevistosModelo) {
        this.casosPrevistosModelo = casosPrevistosModelo;
    }

    public double getIndiceRiscoConsiderado() {
        return indiceRiscoConsiderado;
    }

    public void setIndiceRiscoConsiderado(double indiceRiscoConsiderado) {
        this.indiceRiscoConsiderado = indiceRiscoConsiderado;
    }
}