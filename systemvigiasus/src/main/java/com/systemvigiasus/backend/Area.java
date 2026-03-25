package com.systemvigiasus.backend;

public class Area {

    private Long id;
    private String nome;
    private String unidadeSaude;
    private int totalArmadilhas;
    private int positivas;
    private String risco;

    public Area(Long id, String nome, String unidadeSaude, int totalArmadilhas, int positivas, String risco) {
        this.id = id;
        this.nome = nome;
        this.unidadeSaude = unidadeSaude;
        this.totalArmadilhas = totalArmadilhas;
        this.positivas = positivas;
        this.risco = risco;
    }

    public Long getId() { return id; }
    public String getNome() { return nome; }
    public String getUnidadeSaude() { return unidadeSaude; }
    public int getTotalArmadilhas() { return totalArmadilhas; }
    public int getPositivas() { return positivas; }
    public String getRisco() { return risco; }
}