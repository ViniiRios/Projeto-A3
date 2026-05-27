package com.systemvigiasus.monitoramento.service;

import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.systemvigiasus.monitoramento.domain.Area;
import com.systemvigiasus.monitoramento.dto.AreaCadastroRequestDTO;
import com.systemvigiasus.monitoramento.dto.AreaCadastroResponseDTO;
import com.systemvigiasus.monitoramento.repository.AreaRepository;

class AreaCadastroServiceTest {

    private AreaCadastroService areaCadastroService;
    private AreaRepository areaRepository;

    @BeforeEach
    void setUp() {
        areaRepository = mock(AreaRepository.class);
        areaCadastroService = new AreaCadastroService(areaRepository);
    }

    @Test
    void deveCadastrarAreaComIdGerado() {
        AreaCadastroRequestDTO request = new AreaCadastroRequestDTO(
                "000",
                "Área Centro Sul 1",
                "Centro de Saúde Funcionários",
                "Funcionários",
                "Centro-Sul",
                12000,
                "ATIVA"
        );

        Area areaSalva = new Area(
                1L,
                request.getCodigoArea(),
                request.getNome(),
                request.getUnidadeSaude(),
                request.getBairro(),
                request.getRegionalOuDistrito(),
                request.getPopulacaoReferencia(),
                request.getStatus()
        );

        when(areaRepository.save(any(Area.class))).thenReturn(areaSalva);

        AreaCadastroResponseDTO response = areaCadastroService.cadastrarArea(request);

        assertNotNull(response);
        assertNotNull(response.getId());
        assertEquals(1L, response.getId());
        assertEquals("000", response.getCodigoArea());
        assertEquals("Área Centro Sul 1", response.getNome());
        assertEquals("Centro de Saúde Funcionários", response.getUnidadeSaude());
        assertEquals("Funcionários", response.getBairro());
        assertEquals("Centro-Sul", response.getRegionalOuDistrito());
        assertEquals(12000, response.getPopulacaoReferencia());
        assertEquals("ATIVA", response.getStatus());
    }

    @Test
    void deveListarAreasCadastradas() {
        Area area = new Area(
                1L,
                "001",
                "Área Barreiro 2",
                "Centro de Saúde Tirol",
                "Tirol",
                "Barreiro",
                9800,
                "ATIVA"
        );

        when(areaRepository.findAll()).thenReturn(List.of(area));

        List<AreaCadastroResponseDTO> areas = areaCadastroService.listarAreas();

        assertNotNull(areas);
        assertEquals(1, areas.size());
        assertEquals("001", areas.get(0).getCodigoArea());
        assertEquals("Área Barreiro 2", areas.get(0).getNome());
    }

    @Test
    void deveBuscarAreaPorIdExistente() {
        Area area = new Area(
                1L,
                "002",
                "Área Venda Nova 1",
                "Centro de Saúde Mantiqueira",
                "Mantiqueira",
                "Venda Nova",
                15000,
                "ATIVA"
        );

        when(areaRepository.findById(1L)).thenReturn(Optional.of(area));

        AreaCadastroResponseDTO encontrada = areaCadastroService.buscarPorId(1L);

        assertNotNull(encontrada);
        assertEquals(1L, encontrada.getId());
        assertEquals("002", encontrada.getCodigoArea());
        assertEquals("Área Venda Nova 1", encontrada.getNome());
    }

    @Test
    void deveRetornarNullAoBuscarIdInexistente() {
        when(areaRepository.findById(999L)).thenReturn(Optional.empty());

        AreaCadastroResponseDTO response = areaCadastroService.buscarPorId(999L);

        assertNull(response);
    }
}