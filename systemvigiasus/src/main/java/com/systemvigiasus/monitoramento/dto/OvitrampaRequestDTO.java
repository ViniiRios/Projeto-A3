package com.systemvigiasus.monitoramento.dto;

public class OvitrampaRequestDTO {

    private String codigoArea;
    private String bairro;
    private Integer totalArmadilhas;
    private Integer totalNegativas;
    private Double percentualNegativas;
    private Integer totalPositivas;
    private Double percentualPositivas;

    public OvitrampaRequestDTO() {
    }

    public OvitrampaRequestDTO(String codigoArea, String bairro, Integer totalArmadilhas,
                               Integer totalNegativas, Double percentualNegativas,
                               Integer totalPositivas, Double percentualPositivas) {
        this.codigoArea = codigoArea;
        this.bairro = bairro;
        this.totalArmadilhas = totalArmadilhas;
        this.totalNegativas = totalNegativas;
        this.percentualNegativas = percentualNegativas;
        this.totalPositivas = totalPositivas;
        this.percentualPositivas = percentualPositivas;
    }

    public String getCodigoArea() {
        return codigoArea;
    }

    public void setCodigoArea(String codigoArea) {
        this.codigoArea = codigoArea;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public Integer getTotalArmadilhas() {
        return totalArmadilhas;
    }

    public void setTotalArmadilhas(Integer totalArmadilhas) {
        this.totalArmadilhas = totalArmadilhas;
    }

    public Integer getTotalNegativas() {
        return totalNegativas;
    }

    public void setTotalNegativas(Integer totalNegativas) {
        this.totalNegativas = totalNegativas;
    }

    public Double getPercentualNegativas() {
        return percentualNegativas;
    }

    public void setPercentualNegativas(Double percentualNegativas) {
        this.percentualNegativas = percentualNegativas;
    }

    public Integer getTotalPositivas() {
        return totalPositivas;
    }

    public void setTotalPositivas(Integer totalPositivas) {
        this.totalPositivas = totalPositivas;
    }

    public Double getPercentualPositivas() {
        return percentualPositivas;
    }

    public void setPercentualPositivas(Double percentualPositivas) {
        this.percentualPositivas = percentualPositivas;
    }
}