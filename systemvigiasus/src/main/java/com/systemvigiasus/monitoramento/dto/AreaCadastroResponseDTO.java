package com.systemvigiasus.monitoramento.dto;

public class AreaCadastroResponseDTO {

    private Long id;
    private String nome;
    private String unidadeSaude;
    private String bairro;
    private String regionalOuDistrito;
    private Integer populacaoReferencia;
    private String status;

    public AreaCadastroResponseDTO() {
    }

    public AreaCadastroResponseDTO(Long id, String nome, String unidadeSaude, String bairro,
                                   String regionalOuDistrito, Integer populacaoReferencia, String status) {
        this.id = id;
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