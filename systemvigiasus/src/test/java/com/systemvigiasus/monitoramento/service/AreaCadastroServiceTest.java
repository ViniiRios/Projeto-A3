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
    void deveCadastrarAreaComCodigoGeradoAutomaticamente() {
        Area areaExistente1 = new Area(
                1L,
                "000",
                "Área Norte 1",
                "Centro de Saúde A",
                "AARAO REIS",
                "NORTE",
                12000,
                "ATIVA"
        );

        Area areaExistente2 = new Area(
                2L,
                "001",
                "Área Norte 2",
                "Centro de Saúde B",
                "ALTO VERA CRUZ",
                "NORTE",
                15000,
                "ATIVA"
        );

        AreaCadastroRequestDTO request = new AreaCadastroRequestDTO(
                null,
                "Área Centro Sul 1",
                "Centro de Saúde Funcionários",
                "Funcionários",
                "CENTRO-SUL",
                12000,
                null
        );

        when(areaRepository.findAll()).thenReturn(List.of(areaExistente1, areaExistente2));

        when(areaRepository.save(any(Area.class))).thenAnswer(invocation -> {
            Area area = invocation.getArgument(0);
            area.setId(3L);
            return area;
        });

        AreaCadastroResponseDTO response = areaCadastroService.cadastrarArea(request);

        assertNotNull(response);
        assertNotNull(response.getId());
        assertEquals(3L, response.getId());
        assertEquals("002", response.getCodigoArea());
        assertEquals("Área Centro Sul 1", response.getNome());
        assertEquals("Centro de Saúde Funcionários", response.getUnidadeSaude());
        assertEquals("Funcionários", response.getBairro());
        assertEquals("CENTRO-SUL", response.getRegionalOuDistrito());
        assertEquals(12000, response.getPopulacaoReferencia());
        assertEquals("ATIVA", response.getStatus());
    }

    @Test
    void deveGerarCodigoInicialQuandoNaoExistiremAreas() {
        AreaCadastroRequestDTO request = new AreaCadastroRequestDTO(
                null,
                "Área Inicial",
                "Centro de Saúde Inicial",
                "Bairro Inicial",
                "NORTE",
                10000,
                null
        );

        when(areaRepository.findAll()).thenReturn(List.of());

        when(areaRepository.save(any(Area.class))).thenAnswer(invocation -> {
            Area area = invocation.getArgument(0);
            area.setId(1L);
            return area;
        });

        AreaCadastroResponseDTO response = areaCadastroService.cadastrarArea(request);

        assertNotNull(response);
        assertEquals(1L, response.getId());
        assertEquals("000", response.getCodigoArea());
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

    @Test
    void deveInativarAreaExistente() {
        Area area = new Area(
                70L,
                "069",
                "Área Teste Cadastro Manual",
                "Centro de Saúde Teste",
                "Bairro Teste",
                "NORTE",
                10000,
                "ATIVA"
        );

        when(areaRepository.findById(70L)).thenReturn(Optional.of(area));

        when(areaRepository.save(any(Area.class))).thenAnswer(invocation -> invocation.getArgument(0));

        AreaCadastroResponseDTO response = areaCadastroService.inativarArea(70L);

        assertNotNull(response);
        assertEquals(70L, response.getId());
        assertEquals("069", response.getCodigoArea());
        assertEquals("INATIVA", response.getStatus());
    }

    @Test
    void deveReativarAreaExistente() {
        Area area = new Area(
                70L,
                "069",
                "Área Teste Cadastro Manual",
                "Centro de Saúde Teste",
                "Bairro Teste",
                "NORTE",
                10000,
                "INATIVA"
        );

        when(areaRepository.findById(70L)).thenReturn(Optional.of(area));

        when(areaRepository.save(any(Area.class))).thenAnswer(invocation -> invocation.getArgument(0));

        AreaCadastroResponseDTO response = areaCadastroService.reativarArea(70L);

        assertNotNull(response);
        assertEquals(70L, response.getId());
        assertEquals("069", response.getCodigoArea());
        assertEquals("ATIVA", response.getStatus());
    }
}