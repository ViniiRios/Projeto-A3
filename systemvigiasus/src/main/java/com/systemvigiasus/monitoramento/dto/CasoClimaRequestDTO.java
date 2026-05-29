package com.systemvigiasus.monitoramento.dto;

public class CasoClimaRequestDTO {

    private String periodoReferencia;
    private String regional;
    private Integer casosDengue;
    private Integer casosChikungunya;
    private Integer casosZika;
    private Integer casosTotal;
    private String temperaturaMedia;
    private String precipitacaoTotal;
    private String populacaoRegional;

    public CasoClimaRequestDTO() {
    }

    public CasoClimaRequestDTO(String periodoReferencia, String regional, Integer casosDengue,
                               Integer casosChikungunya, Integer casosZika, Integer casosTotal,
                               String temperaturaMedia, String precipitacaoTotal, String populacaoRegional) {
        this.periodoReferencia = periodoReferencia;
        this.regional = regional;
        this.casosDengue = casosDengue;
        this.casosChikungunya = casosChikungunya;
        this.casosZika = casosZika;
        this.casosTotal = casosTotal;
        this.temperaturaMedia = temperaturaMedia;
        this.precipitacaoTotal = precipitacaoTotal;
        this.populacaoRegional = populacaoRegional;
    }

    public String getPeriodoReferencia() {
        return periodoReferencia;
    }

    public void setPeriodoReferencia(String periodoReferencia) {
        this.periodoReferencia = periodoReferencia;
    }

    public String getRegional() {
        return regional;
    }

    public void setRegional(String regional) {
        this.regional = regional;
    }

    public Integer getCasosDengue() {
        return casosDengue;
    }

    public void setCasosDengue(Integer casosDengue) {
        this.casosDengue = casosDengue;
    }

    public Integer getCasosChikungunya() {
        return casosChikungunya;
    }

    public void setCasosChikungunya(Integer casosChikungunya) {
        this.casosChikungunya = casosChikungunya;
    }

    public Integer getCasosZika() {
        return casosZika;
    }

    public void setCasosZika(Integer casosZika) {
        this.casosZika = casosZika;
    }

    public Integer getCasosTotal() {
        return casosTotal;
    }

    public void setCasosTotal(Integer casosTotal) {
        this.casosTotal = casosTotal;
    }

    public String getTemperaturaMedia() {
        return temperaturaMedia;
    }

    public void setTemperaturaMedia(String temperaturaMedia) {
        this.temperaturaMedia = temperaturaMedia;
    }

    public String getPrecipitacaoTotal() {
        return precipitacaoTotal;
    }

    public void setPrecipitacaoTotal(String precipitacaoTotal) {
        this.precipitacaoTotal = precipitacaoTotal;
    }

    public String getPopulacaoRegional() {
        return populacaoRegional;
    }

    public void setPopulacaoRegional(String populacaoRegional) {
        this.populacaoRegional = populacaoRegional;
    }
}