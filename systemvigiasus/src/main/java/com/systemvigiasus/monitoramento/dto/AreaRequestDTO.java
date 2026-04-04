package com.systemvigiasus.monitoramento.dto;

public class AreaRequestDTO {

    private Long id;
    private String nome;
    private int numeroCasos;
    private int populacao;

    public AreaRequestDTO() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public int getNumeroCasos() { return numeroCasos; }
    public void setNumeroCasos(int numeroCasos) { this.numeroCasos = numeroCasos; }

    public int getPopulacao() { return populacao; }
    public void setPopulacao(int populacao) { this.populacao = populacao; }

    public AreaRequestDTO(Long id, String nome, int numeroCasos, int populacao) {
        this.id = id;
        this.nome = nome;
        this.numeroCasos = numeroCasos;
        this.populacao = populacao;
    }
}