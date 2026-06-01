package com.systemvigiasus.monitoramento.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.systemvigiasus.monitoramento.domain.Usuario;

@Repository
public interface UsuarioRepository extends JpaRepository<Usuario, Long> {

    Optional<Usuario> findByUsernameIgnoreCaseAndSenhaAndStatus(String username, String senha, String status);

    boolean existsByUsernameIgnoreCase(String username);
}