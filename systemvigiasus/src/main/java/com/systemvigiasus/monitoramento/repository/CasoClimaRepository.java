package com.systemvigiasus.monitoramento.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.systemvigiasus.monitoramento.domain.CasoClima;

@Repository
public interface CasoClimaRepository extends JpaRepository<CasoClima, Long> {
}