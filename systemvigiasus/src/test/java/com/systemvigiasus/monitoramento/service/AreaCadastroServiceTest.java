package com.systemvigiasus.monitoramento.service;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.systemvigiasus.monitoramento.dto.AreaCadastroRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaCadastroResponseDTO;

class AreaCadastroServiceTest {

    private AreaCadastroService areaCadastroService;

    @BeforeEach
    void setUp() {
        areaCadastroService = new AreaCadastroService();
    }

    @Test
    void deveCadastrarAreaComIdGerado() {
        AreaCadastroRequestDTO request = new AreaCadastroRequestDTO(
                "Área Centro Sul 1",
                "Centro de Saúde Funcionários",
                "Funcionários",
                "Centro-Sul",
                12000,
                "ATIVA"
        );

        AreaCadastroResponseDTO response = areaCadastroService.cadastrarArea(request);

        assertNotNull(response);
        assertNotNull(response.getId());
        assertEquals("Área Centro Sul 1", response.getNome());
        assertEquals("Centro de Saúde Funcionários", response.getUnidadeSaude());
        assertEquals("Funcionários", response.getBairro());
        assertEquals("Centro-Sul", response.getRegionalOuDistrito());
        assertEquals(12000, response.getPopulacaoReferencia());
        assertEquals("ATIVA", response.getStatus());
    }

    @Test
    void deveListarAreasCadastradas() {
        AreaCadastroRequestDTO request = new AreaCadastroRequestDTO(
                "Área Barreiro 2",
                "Centro de Saúde Tirol",
                "Tirol",
                "Barreiro",
                9800,
                "ATIVA"
        );

        areaCadastroService.cadastrarArea(request);

        List<AreaCadastroResponseDTO> areas = areaCadastroService.listarAreas();

        assertNotNull(areas);
        assertEquals(1, areas.size());
        assertEquals("Área Barreiro 2", areas.get(0).getNome());
    }

    @Test
    void deveBuscarAreaPorIdExistente() {
        AreaCadastroRequestDTO request = new AreaCadastroRequestDTO(
                "Área Venda Nova 1",
                "Centro de Saúde Mantiqueira",
                "Mantiqueira",
                "Venda Nova",
                15000,
                "ATIVA"
        );

        AreaCadastroResponseDTO cadastrada = areaCadastroService.cadastrarArea(request);
        AreaCadastroResponseDTO encontrada = areaCadastroService.buscarPorId(cadastrada.getId());

        assertNotNull(encontrada);
        assertEquals(cadastrada.getId(), encontrada.getId());
        assertEquals("Área Venda Nova 1", encontrada.getNome());
    }

    @Test
    void deveRetornarNullAoBuscarIdInexistente() {
        AreaCadastroResponseDTO response = areaCadastroService.buscarPorId(999L);

        assertNull(response);
    }
}