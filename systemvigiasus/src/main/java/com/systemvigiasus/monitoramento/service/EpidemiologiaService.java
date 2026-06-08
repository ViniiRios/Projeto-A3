package com.systemvigiasus.monitoramento.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.systemvigiasus.monitoramento.dto.AreaRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaResponseDTO;
import com.systemvigiasus.monitoramento.dto.IAPredictionRequest;
import com.systemvigiasus.monitoramento.dto.IAPredictionResponse;

@Service
public class EpidemiologiaService {

    @Autowired
    private IAIntegrationService iaService;

    public AreaResponseDTO calcularRiscoArea(AreaRequestDTO request) {
        double casos = (double) request.getNumeroCasos();
        double populacao = (double) request.getPopulacao();

        double taxaAtual = calcularTaxaIncidencia(casos, populacao);

        double temperaturaLag1 = limitar(request.getTemperatura(), 15.0, 30.0);
        double temperaturaLag2 = limitar(temperaturaLag1 - 2.0, 15.0, 30.0);

        double precipitacaoLag1 = Math.max(request.getChuva(), 0.0);
        double precipitacaoLag2 = Math.max(precipitacaoLag1 - 50.0, 0.0);

        double pressaoLag1 = 900.0;
        double pressaoLag2 = 900.5;

        IAPredictionRequest iaRequest = new IAPredictionRequest(
            request.getMes(),
            request.getAno(),
            request.getNumeroCasos(),
            request.getCasosLag2(),
            temperaturaLag1,
            temperaturaLag2,
            precipitacaoLag1,
            precipitacaoLag2,
            pressaoLag1,
            pressaoLag2,
            request.getPopulacao()
        );

        IAPredictionResponse previsao = iaService.obterPrevisaoDaIA(iaRequest);

        double taxaPrevistaModelo = previsao.taxaPrevistaModelo();
        double casosPrevistosModelo = previsao.casosPrevistosModelo();

        double indiceRiscoConsiderado = previsao.indiceRiscoConsiderado();

        if (indiceRiscoConsiderado <= 0.0) {
            indiceRiscoConsiderado = previsao.taxaIncidencia();
        }

        if (indiceRiscoConsiderado <= 0.0) {
            indiceRiscoConsiderado = taxaAtual;
        }

        String risco = previsao.risco();

        if (risco == null || risco.isBlank()) {
            risco = classificarRisco(indiceRiscoConsiderado);
        }

        return new AreaResponseDTO(
            request.getId(),
            request.getNome(),
            risco,
            indiceRiscoConsiderado,
            taxaAtual,
            taxaPrevistaModelo,
            casosPrevistosModelo,
            indiceRiscoConsiderado
        );
    }

    private double calcularTaxaIncidencia(double casos, double populacao) {
        if (populacao > 0) {
            return (casos * 100000.0) / populacao;
        }

        return 0.0;
    }

    private double limitar(double valor, double minimo, double maximo) {
        return Math.max(minimo, Math.min(valor, maximo));
    }

    private String classificarRisco(double indiceRisco) {
        if (indiceRisco >= 300.0) {
            return "ALERTA MÁXIMO";
        }

        if (indiceRisco >= 100.0) {
            return "RISCO MODERADO";
        }

        return "RISCO BAIXO";
    }
}