package com.systemvigiasus.monitoramento.dto;

public class OvitrampaResponseDTO {

    private Long id;
    private String codigoArea;
    private String bairro;
    private Integer totalArmadilhas;
    private Integer totalNegativas;
    private Double percentualNegativas;
    private Integer totalPositivas;
    private Double percentualPositivas;

    public OvitrampaResponseDTO() {
    }

    public OvitrampaResponseDTO(Long id, String codigoArea, String bairro, Integer totalArmadilhas,
                                Integer totalNegativas, Double percentualNegativas,
                                Integer totalPositivas, Double percentualPositivas) {
        this.id = id;
        this.codigoArea = codigoArea;
        this.bairro = bairro;
        this.totalArmadilhas = totalArmadilhas;
        this.totalNegativas = totalNegativas;
        this.percentualNegativas = percentualNegativas;
        this.totalPositivas = totalPositivas;
        this.percentualPositivas = percentualPositivas;
    }

    public Long getId() {
        return id;
    }

    public String getCodigoArea() {
        return codigoArea;
    }

    public String getBairro() {
        return bairro;
    }

    public Integer getTotalArmadilhas() {
        return totalArmadilhas;
    }

    public Integer getTotalNegativas() {
        return totalNegativas;
    }

    public Double getPercentualNegativas() {
        return percentualNegativas;
    }

    public Integer getTotalPositivas() {
        return totalPositivas;
    }

    public Double getPercentualPositivas() {
        return percentualPositivas;
    }
}