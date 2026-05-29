package com.systemvigiasus.monitoramento.dto;

public class CasoClimaResponseDTO {

    private Long id;
    private String periodoReferencia;
    private String regional;
    private Integer casosDengue;
    private Integer casosChikungunya;
    private Integer casosZika;
    private Integer casosTotal;
    private String temperaturaMedia;
    private String precipitacaoTotal;
    private String populacaoRegional;

    public CasoClimaResponseDTO() {
    }

    public CasoClimaResponseDTO(Long id, String periodoReferencia, String regional, Integer casosDengue,
                                Integer casosChikungunya, Integer casosZika, Integer casosTotal,
                                String temperaturaMedia, String precipitacaoTotal, String populacaoRegional) {
        this.id = id;
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

    public Long getId() {
        return id;
    }

    public String getPeriodoReferencia() {
        return periodoReferencia;
    }

    public String getRegional() {
        return regional;
    }

    public Integer getCasosDengue() {
        return casosDengue;
    }

    public Integer getCasosChikungunya() {
        return casosChikungunya;
    }

    public Integer getCasosZika() {
        return casosZika;
    }

    public Integer getCasosTotal() {
        return casosTotal;
    }

    public String getTemperaturaMedia() {
        return temperaturaMedia;
    }

    public String getPrecipitacaoTotal() {
        return precipitacaoTotal;
    }

    public String getPopulacaoRegional() {
        return populacaoRegional;
    }
}