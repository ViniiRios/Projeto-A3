package com.systemvigiasus.monitoramento.dto;

public class LoginRequestDTO {

    private String username;
    private String senha;

    public LoginRequestDTO() {
    }

    public LoginRequestDTO(String username, String senha) {
        this.username = username;
        this.senha = senha;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }
}