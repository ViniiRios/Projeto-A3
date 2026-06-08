package com.systemvigiasus.monitoramento.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.systemvigiasus.monitoramento.domain.Area;

@Repository
public interface AreaRepository extends JpaRepository<Area, Long> {
}