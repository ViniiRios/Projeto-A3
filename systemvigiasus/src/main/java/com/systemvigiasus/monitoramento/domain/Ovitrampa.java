package com.systemvigiasus.monitoramento.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "ovitrampas")
public class Ovitrampa {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "codigo_area", nullable = false)
    private String codigoArea;

    @Column(nullable = false)
    private String bairro;

    @Column(name = "total_armadilhas", nullable = false)
    private Integer totalArmadilhas;

    @Column(name = "total_negativas", nullable = false)
    private Integer totalNegativas;

    @Column(name = "percentual_negativas", nullable = false)
    private Double percentualNegativas;

    @Column(name = "total_positivas", nullable = false)
    private Integer totalPositivas;

    @Column(name = "percentual_positivas", nullable = false)
    private Double percentualPositivas;

    public Ovitrampa() {
    }

    public Ovitrampa(Long id, String codigoArea, String bairro, Integer totalArmadilhas,
                     Integer totalNegativas, Double percentualNegativas,
                     Integer totalPositivas, Double percentualPositivas) {
        this.id = id;
        this.codigoArea = codigoArea;
        this.bairro = bairro;
        this.totalArmadilhas = totalArmadilhas;
        this.totalNegativas = totalNegativas;
        this.percentualNegativas = percentualNegativas;
        this.totalPositivas = totalPositivas;
        this.percentualPositivas = percentualPositivas;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
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