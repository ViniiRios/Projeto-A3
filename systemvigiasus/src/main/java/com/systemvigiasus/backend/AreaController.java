package com.systemvigiasus.backend;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AreaController {

    @GetMapping("/areas")
    public List<Area> listarAreas() {
        return List.of(
                new Area(1L, "Centro-Sul", "Centro de Saúde A", 20, 12, "Alto"),
                new Area(2L, "Norte", "Centro de Saúde B", 15, 5, "Moderado"),
                new Area(3L, "Leste", "Centro de Saúde C", 10, 2, "Baixo")
        );
    }
}