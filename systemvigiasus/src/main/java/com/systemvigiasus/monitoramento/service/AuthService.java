package com.systemvigiasus.monitoramento.service;

import org.springframework.stereotype.Service;

import com.systemvigiasus.monitoramento.domain.Usuario;
import com.systemvigiasus.monitoramento.dto.LoginRequestDTO;
import com.systemvigiasus.monitoramento.dto.LoginResponseDTO;
import com.systemvigiasus.monitoramento.repository.UsuarioRepository;

import jakarta.annotation.PostConstruct;

@Service
public class AuthService {

    private static final String STATUS_ATIVO = "ATIVO";

    private final UsuarioRepository usuarioRepository;

    public AuthService(UsuarioRepository usuarioRepository) {
        this.usuarioRepository = usuarioRepository;
    }

    @PostConstruct
    public void inicializarUsuariosPadrao() {
        criarUsuarioPadraoSeNaoExistir(
                "Daniela Teixeira Abreu",
                "daniela",
                "1234",
                "Gestor de TI"
        );

        criarUsuarioPadraoSeNaoExistir(
                "Vinícius Raphael Rios",
                "vinicius",
                "1234",
                "Gestor Epidemiológico"
        );

        criarUsuarioPadraoSeNaoExistir(
                "Matheus Felipe Lopes",
                "matheus",
                "1234",
                "Analista de Dados"
        );

        criarUsuarioPadraoSeNaoExistir(
                "Nátali Isaltino Gomes",
                "natali",
                "1234",
                "Operador de Importação"
        );

        criarUsuarioPadraoSeNaoExistir(
                "Marcela Maria Barbosa",
                "marcela",
                "1234",
                "Analista de Vigilância"
        );
    }

    public LoginResponseDTO autenticar(LoginRequestDTO request) {
        if (request == null || request.getUsername() == null || request.getSenha() == null) {
            return null;
        }

        return usuarioRepository
                .findByUsernameIgnoreCaseAndSenhaAndStatus(
                        request.getUsername().trim(),
                        request.getSenha(),
                        STATUS_ATIVO
                )
                .map(this::converterParaResponse)
                .orElse(null);
    }

    private void criarUsuarioPadraoSeNaoExistir(String nome, String username, String senha, String perfil) {
        if (!usuarioRepository.existsByUsernameIgnoreCase(username)) {
            Usuario usuario = new Usuario(
                    null,
                    nome,
                    username,
                    senha,
                    perfil,
                    STATUS_ATIVO
            );

            usuarioRepository.save(usuario);
        }
    }

    private LoginResponseDTO converterParaResponse(Usuario usuario) {
        return new LoginResponseDTO(
                usuario.getId(),
                usuario.getNome(),
                usuario.getUsername(),
                usuario.getPerfil(),
                usuario.getStatus()
        );
    }
}