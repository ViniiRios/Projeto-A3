package com.systemvigiasus.monitoramento.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "areas")
public class Area {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "codigo_area", unique = true)
    private String codigoArea;

    @Column(nullable = false)
    private String nome;

    @Column(nullable = false)
    private String unidadeSaude;

    @Column(nullable = false)
    private String bairro;

    @Column(nullable = false)
    private String regionalOuDistrito;

    @Column(nullable = false)
    private Integer populacaoReferencia;

    @Column(nullable = false)
    private String status;

    public Area() {
    }

    public Area(Long id, String codigoArea, String nome, String unidadeSaude, String bairro,
                String regionalOuDistrito, Integer populacaoReferencia, String status) {
        this.id = id;
        this.codigoArea = codigoArea;
        this.nome = nome;
        this.unidadeSaude = unidadeSaude;
        this.bairro = bairro;
        this.regionalOuDistrito = regionalOuDistrito;
        this.populacaoReferencia = populacaoReferencia;
        this.status = status;
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

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getUnidadeSaude() {
        return unidadeSaude;
    }

    public void setUnidadeSaude(String unidadeSaude) {
        this.unidadeSaude = unidadeSaude;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getRegionalOuDistrito() {
        return regionalOuDistrito;
    }

    public void setRegionalOuDistrito(String regionalOuDistrito) {
        this.regionalOuDistrito = regionalOuDistrito;
    }

    public Integer getPopulacaoReferencia() {
        return populacaoReferencia;
    }

    public void setPopulacaoReferencia(Integer populacaoReferencia) {
        this.populacaoReferencia = populacaoReferencia;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}