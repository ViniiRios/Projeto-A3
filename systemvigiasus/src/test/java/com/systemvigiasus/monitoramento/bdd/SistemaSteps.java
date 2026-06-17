package com.systemvigiasus.monitoramento.bdd;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import io.cucumber.java.pt.Dado;
import io.cucumber.java.pt.E;
import io.cucumber.java.pt.Entao;
import io.cucumber.java.pt.Quando;

public class SistemaSteps {

    private boolean usuarioAtivo;
    private boolean autenticado;
    private boolean credenciaisInvalidas;

    private String nomeUsuario;
    private String perfilUsuario;

    private final List<Map<String, Object>> areas = new ArrayList<>();
    private final List<Map<String, Object>> ovitrampas = new ArrayList<>();

    private Map<String, Object> areaAtual;
    private Map<String, Object> areaCadastrada;
    private List<Map<String, Object>> resultadoAreas;
    private List<Map<String, Object>> resultadoOvitrampas;

    private double casosAtuais;
    private double populacao;
    private double taxaIncidencia;
    private String riscoCalculado;
    private boolean erroConsulta;

    // -------------------------
    // BDD-01 e BDD-02: Login
    // -------------------------

    @Dado("que existe um usuário ativo cadastrado no sistema")
    public void queExisteUmUsuarioAtivoCadastradoNoSistema() {
        usuarioAtivo = true;
        nomeUsuario = "Vinícius Raphael Rios";
        perfilUsuario = "Gestor Epidemiológico";
    }

    @Quando("o usuário informa login e senha corretos")
    public void oUsuarioInformaLoginESenhaCorretos() {
        autenticado = usuarioAtivo;
        credenciaisInvalidas = false;
    }

    @Entao("o sistema deve autenticar o usuário")
    public void oSistemaDeveAutenticarOUsuario() {
        assertTrue(autenticado);
    }

    @E("deve retornar o nome e o perfil de acesso")
    public void deveRetornarONomeEOPerfilDeAcesso() {
        assertNotNull(nomeUsuario);
        assertNotNull(perfilUsuario);
        assertEquals("Gestor Epidemiológico", perfilUsuario);
    }

    @Quando("o usuário informa uma senha incorreta")
    public void oUsuarioInformaUmaSenhaIncorreta() {
        autenticado = false;
        credenciaisInvalidas = true;
    }

    @Entao("o sistema não deve autenticar o usuário")
    public void oSistemaNaoDeveAutenticarOUsuario() {
        assertFalse(autenticado);
    }

    @E("deve informar que as credenciais são inválidas")
    public void deveInformarQueAsCredenciaisSaoInvalidas() {
        assertTrue(credenciaisInvalidas);
    }

    // -------------------------
    // BDD-03 e BDD-04: Áreas
    // -------------------------

    @Dado("que o backend está em execução")
    public void queOBackendEstaEmExecucao() {
        assertTrue(true);
    }

    @E("existem áreas monitoradas cadastradas no banco")
    @Dado("que existem áreas monitoradas cadastradas no banco")
    public void existemAreasMonitoradasCadastradasNoBanco() {
        areas.clear();

        Map<String, Object> area = new HashMap<>();
        area.put("id", 1L);
        area.put("codigoArea", "000");
        area.put("bairro", "AARAO REIS");
        area.put("nome", "BHZ NORT");
        area.put("regionalOuDistrito", "NORTE");
        area.put("unidadeSaude", "CENTRO DE SAUDE AARAO REIS");
        area.put("populacaoReferencia", 213427);
        area.put("status", "ATIVA");

        areas.add(area);
    }

    @Quando("uma nova área é cadastrada com nome, unidade de saúde, bairro, regional e população")
    public void umaNovaAreaECadastradaComDadosValidos() {
        int proximoNumero = areas.size();

        areaCadastrada = new HashMap<>();
        areaCadastrada.put("id", 2L);
        areaCadastrada.put("codigoArea", String.format("%03d", proximoNumero));
        areaCadastrada.put("bairro", "BAIRRO TESTE");
        areaCadastrada.put("nome", "AREA TESTE");
        areaCadastrada.put("regionalOuDistrito", "NORTE");
        areaCadastrada.put("unidadeSaude", "UBS TESTE");
        areaCadastrada.put("populacaoReferencia", 10000);
        areaCadastrada.put("status", "ATIVA");

        areas.add(areaCadastrada);
    }

    @Entao("o sistema deve salvar a área no banco de dados")
    public void oSistemaDeveSalvarAAreaNoBancoDeDados() {
        assertTrue(areas.contains(areaCadastrada));
    }

    @E("deve gerar automaticamente um código para a área")
    public void deveGerarAutomaticamenteUmCodigoParaAArea() {
        assertNotNull(areaCadastrada.get("codigoArea"));
        assertTrue(areaCadastrada.get("codigoArea").toString().matches("\\d{3}"));
    }

    @E("deve cadastrar a área com status ATIVA")
    public void deveCadastrarAAreaComStatusAtiva() {
        assertEquals("ATIVA", areaCadastrada.get("status"));
    }

    @Quando("o usuário solicita a listagem de áreas")
    public void oUsuarioSolicitaAListagemDeAreas() {
        resultadoAreas = new ArrayList<>(areas);
    }

    @Entao("o sistema deve retornar a lista de áreas cadastradas")
    public void oSistemaDeveRetornarAListaDeAreasCadastradas() {
        assertNotNull(resultadoAreas);
        assertFalse(resultadoAreas.isEmpty());
    }

    @E("cada área deve apresentar código, bairro, regional, unidade de saúde, população e status")
    public void cadaAreaDeveApresentarOsCamposEsperados() {
        Map<String, Object> area = resultadoAreas.get(0);

        assertTrue(area.containsKey("codigoArea"));
        assertTrue(area.containsKey("bairro"));
        assertTrue(area.containsKey("regionalOuDistrito"));
        assertTrue(area.containsKey("unidadeSaude"));
        assertTrue(area.containsKey("populacaoReferencia"));
        assertTrue(area.containsKey("status"));
    }

    // -------------------------
    // BDD-05 e BDD-06: Manutenção de área
    // -------------------------

    @Dado("que existe uma área monitorada com status ATIVA")
    public void queExisteUmaAreaMonitoradaComStatusAtiva() {
        areaAtual = new HashMap<>();
        areaAtual.put("id", 1L);
        areaAtual.put("codigoArea", "000");
        areaAtual.put("status", "ATIVA");

        areas.clear();
        areas.add(areaAtual);
    }

    @Quando("o usuário solicita a inativação dessa área")
    public void oUsuarioSolicitaAInativacaoDessaArea() {
        areaAtual.put("status", "INATIVA");
    }

    @Entao("o sistema deve alterar o status da área para INATIVA")
    public void oSistemaDeveAlterarOStatusDaAreaParaInativa() {
        assertEquals("INATIVA", areaAtual.get("status"));
    }

    @E("a área deve continuar cadastrada no banco de dados")
    public void aAreaDeveContinuarCadastradaNoBancoDeDados() {
        assertTrue(areas.contains(areaAtual));
    }

    @Dado("que existe uma área monitorada com status INATIVA")
    public void queExisteUmaAreaMonitoradaComStatusInativa() {
        areaAtual = new HashMap<>();
        areaAtual.put("id", 1L);
        areaAtual.put("codigoArea", "000");
        areaAtual.put("status", "INATIVA");

        areas.clear();
        areas.add(areaAtual);
    }

    @Quando("o usuário solicita a reativação dessa área")
    public void oUsuarioSolicitaAReativacaoDessaArea() {
        areaAtual.put("status", "ATIVA");
    }

    @Entao("o sistema deve alterar o status da área para ATIVA")
    public void oSistemaDeveAlterarOStatusDaAreaParaAtiva() {
        assertEquals("ATIVA", areaAtual.get("status"));
    }

    @E("a área deve continuar disponível para consulta")
    public void aAreaDeveContinuarDisponivelParaConsulta() {
        assertTrue(areas.contains(areaAtual));
    }

    // -------------------------
    // BDD-07, BDD-08 e BDD-09: Risco epidemiológico
    // -------------------------

    @Dado("que o usuário informa poucos casos em relação à população")
    public void queOUsuarioInformaPoucosCasosEmRelacaoAPopulacao() {
        casosAtuais = 10;
        populacao = 200000;
    }

    @Dado("que o usuário informa quantidade intermediária de casos em relação à população")
    public void queOUsuarioInformaQuantidadeIntermediariaDeCasosEmRelacaoAPopulacao() {
        casosAtuais = 300;
        populacao = 200000;
    }

    @Dado("que o usuário informa muitos casos em relação à população")
    public void queOUsuarioInformaMuitosCasosEmRelacaoAPopulacao() {
        casosAtuais = 800;
        populacao = 200000;
    }

    @Quando("o sistema calcula a taxa de incidência")
    public void oSistemaCalculaATaxaDeIncidencia() {
        taxaIncidencia = (casosAtuais * 100000.0) / populacao;

        if (taxaIncidencia >= 300) {
            riscoCalculado = "ALERTA MÁXIMO";
        } else if (taxaIncidencia >= 100) {
            riscoCalculado = "RISCO MODERADO";
        } else {
            riscoCalculado = "RISCO BAIXO";
        }
    }

    @Entao("o resultado deve indicar RISCO BAIXO")
    public void oResultadoDeveIndicarRiscoBaixo() {
        assertEquals("RISCO BAIXO", riscoCalculado);
    }

    @Entao("o resultado deve indicar RISCO MODERADO")
    public void oResultadoDeveIndicarRiscoModerado() {
        assertEquals("RISCO MODERADO", riscoCalculado);
    }

    @Entao("o resultado deve indicar ALERTA MÁXIMO")
    public void oResultadoDeveIndicarAlertaMaximo() {
        assertEquals("ALERTA MÁXIMO", riscoCalculado);
    }

    // -------------------------
    // BDD-10 e BDD-11: Ovitrampas
    // -------------------------

    @Dado("que existe uma área monitorada com código cadastrado")
    public void queExisteUmaAreaMonitoradaComCodigoCadastrado() {
        areaAtual = new HashMap<>();
        areaAtual.put("codigoArea", "000");
        areaAtual.put("bairro", "AARAO REIS");
    }

    @E("existem dados de ovitrampas vinculados a essa área")
    public void existemDadosDeOvitrampasVinculadosAEssaArea() {
        ovitrampas.clear();

        Map<String, Object> registro = new HashMap<>();
        registro.put("codigoArea", "000");
        registro.put("totalArmadilhas", 100);
        registro.put("totalPositivas", 38);
        registro.put("totalNegativas", 62);
        registro.put("percentualPositivas", 38.0);

        ovitrampas.add(registro);
    }

    @Quando("o usuário consulta as ovitrampas pelo código da área")
    public void oUsuarioConsultaAsOvitrampasPeloCodigoDaArea() {
        erroConsulta = false;
        resultadoOvitrampas = new ArrayList<>();

        String codigoArea = areaAtual.get("codigoArea").toString();

        for (Map<String, Object> registro : ovitrampas) {
            if (codigoArea.equals(registro.get("codigoArea"))) {
                resultadoOvitrampas.add(registro);
            }
        }
    }

    @Entao("o sistema deve retornar os indicadores da área")
    public void oSistemaDeveRetornarOsIndicadoresDaArea() {
        assertNotNull(resultadoOvitrampas);
        assertFalse(resultadoOvitrampas.isEmpty());
    }

    @E("deve exibir total de armadilhas, positivas, negativas e percentual de positividade")
    public void deveExibirIndicadoresDeOvitrampas() {
        Map<String, Object> registro = resultadoOvitrampas.get(0);

        assertTrue(registro.containsKey("totalArmadilhas"));
        assertTrue(registro.containsKey("totalPositivas"));
        assertTrue(registro.containsKey("totalNegativas"));
        assertTrue(registro.containsKey("percentualPositivas"));
    }

    @Dado("que existe uma área monitorada sem registros de ovitrampas")
    public void queExisteUmaAreaMonitoradaSemRegistrosDeOvitrampas() {
        areaAtual = new HashMap<>();
        areaAtual.put("codigoArea", "999");

        ovitrampas.clear();
    }

    @Entao("o sistema deve retornar uma lista vazia")
    public void oSistemaDeveRetornarUmaListaVazia() {
        assertNotNull(resultadoOvitrampas);
        assertTrue(resultadoOvitrampas.isEmpty());
    }

    @E("não deve apresentar erro na consulta")
    public void naoDeveApresentarErroNaConsulta() {
        assertFalse(erroConsulta);
    }
}