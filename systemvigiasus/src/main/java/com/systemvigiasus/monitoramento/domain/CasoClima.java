package com.systemvigiasus.monitoramento.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "casos_clima")
public class CasoClima {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "periodo_referencia", nullable = false)
    private String periodoReferencia;

    @Column(nullable = false)
    private String regional;

    @Column(name = "casos_dengue", nullable = false)
    private Integer casosDengue;

    @Column(name = "casos_chikungunya", nullable = false)
    private Integer casosChikungunya;

    @Column(name = "casos_zika", nullable = false)
    private Integer casosZika;

    @Column(name = "casos_total", nullable = false)
    private Integer casosTotal;

    @Column(name = "temperatura_media", nullable = false)
    private String temperaturaMedia;

    @Column(name = "precipitacao_total", nullable = false)
    private String precipitacaoTotal;

    @Column(name = "populacao_regional", nullable = false)
    private String populacaoRegional;

    public CasoClima() {
    }

    public CasoClima(Long id, String periodoReferencia, String regional, Integer casosDengue,
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