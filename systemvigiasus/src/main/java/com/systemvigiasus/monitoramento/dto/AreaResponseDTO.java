package com.systemvigiasus.monitoramento.dto;

public class AreaResponseDTO {

    private Long id;
    private String nome;
    private String risco; 

    public AreaResponseDTO() {}

    public AreaResponseDTO(Long id, String nome, String risco) {
        this.id = id;
        this.nome = nome;
        this.risco = risco;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getRisco() { return risco; }
    public void setRisco(String risco) { this.risco = risco; }
}