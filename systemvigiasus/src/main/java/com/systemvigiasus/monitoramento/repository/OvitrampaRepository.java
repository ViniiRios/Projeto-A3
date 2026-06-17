package com.systemvigiasus.monitoramento.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.systemvigiasus.monitoramento.domain.Ovitrampa;

@Repository
public interface OvitrampaRepository extends JpaRepository<Ovitrampa, Long> {

    List<Ovitrampa> findByCodigoArea(String codigoArea);
}