package com.systemvigiasus.monitoramento.dto;

public class LoginResponseDTO {

    private Long id;
    private String nome;
    private String username;
    private String perfil;
    private String status;

    public LoginResponseDTO() {
    }

    public LoginResponseDTO(Long id, String nome, String username, String perfil, String status) {
        this.id = id;
        this.nome = nome;
        this.username = username;
        this.perfil = perfil;
        this.status = status;
    }

    public Long getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public String getUsername() {
        return username;
    }

    public String getPerfil() {
        return perfil;
    }

    public String getStatus() {
        return status;
    }
}