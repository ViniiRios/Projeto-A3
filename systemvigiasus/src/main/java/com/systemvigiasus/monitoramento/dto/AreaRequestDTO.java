package com.systemvigiasus.monitoramento.dto;

public class AreaRequestDTO {
    
    private String nome;
    private String unidadeSaude;
    private int totalArmadilhas;
    private int positivas;

    public AreaRequestDTO() {}

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getUnidadeSaude() { return unidadeSaude; }
    public void setUnidadeSaude(String unidadeSaude) { this.unidadeSaude = unidadeSaude; }

    public int getTotalArmadilhas() { return totalArmadilhas; }
    public void setTotalArmadilhas(int totalArmadilhas) { this.totalArmadilhas = totalArmadilhas; }

    public int getPositivas() { return positivas; }
    public void setPositivas(int positivas) { this.positivas = positivas; }
}