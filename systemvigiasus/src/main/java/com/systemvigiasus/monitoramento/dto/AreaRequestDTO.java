package com.systemvigiasus.monitoramento.dto;

public class AreaRequestDTO {

    private Long id;
    private String nome;
    private int numeroCasos;
    private int populacao;

    private int mes;
    private int ano;
    private int casosLag2;
    private double temperatura;
    private double chuva;

    public AreaRequestDTO() {}

    public AreaRequestDTO(Long id, String nome, Integer numeroCasos, int populacao, int mes, int ano, int casosLag2, Double temperatura, Double chuva) {
        this.id = id;
        this.nome = nome;
        this.numeroCasos = numeroCasos;
        this.populacao = populacao;
        this.mes = mes;
        this.ano = ano;
        this.casosLag2 = casosLag2;
        this.temperatura = temperatura;
        this.chuva = chuva;
    }

    public AreaRequestDTO(double temperatura, double chuva, int numeroCasos) {
    this.temperatura = temperatura;
    this.chuva = chuva;
    this.numeroCasos = numeroCasos;

    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public int getNumeroCasos() { return numeroCasos; }
    public void setNumeroCasos(int numeroCasos) { this.numeroCasos = numeroCasos; }

    public int getPopulacao() { return populacao; }
    public void setPopulacao(int populacao) { this.populacao = populacao; }

    public int getMes() { return mes; }
    public void setMes(int mes) { this.mes = mes; }

    public int getAno() { return ano; }
    public void setAno(int ano) { this.ano = ano; }

    public int getCasosLag2() { return casosLag2; }
    public void setCasosLag2(int casosLag2) { this.casosLag2 = casosLag2; }

    public double getTemperatura() { return temperatura; }
    public void setTemperatura(double temperatura) { this.temperatura = temperatura; }

    public double getChuva() { return chuva; }
    public void setChuva(double chuva) { this.chuva = chuva; }

}