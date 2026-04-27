package com.systemvigiasus.monitoramento.dto;

public class AreaCadastroRequestDTO {

    private String nome;
    private String unidadeSaude;
    private String bairro;
    private String regionalOuDistrito;
    private Integer populacaoReferencia;
    private String status;

    public AreaCadastroRequestDTO() {
    }

    public AreaCadastroRequestDTO(String nome, String unidadeSaude, String bairro,
                                  String regionalOuDistrito, Integer populacaoReferencia, String status) {
        this.nome = nome;
        this.unidadeSaude = unidadeSaude;
        this.bairro = bairro;
        this.regionalOuDistrito = regionalOuDistrito;
        this.populacaoReferencia = populacaoReferencia;
        this.status = status;
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