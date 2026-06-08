# language: pt

Funcionalidade: Autenticação de usuários
  Como usuário do sistema
  Quero acessar a plataforma com login e senha
  Para visualizar os módulos permitidos conforme meu perfil

  @BDD-01
  Cenário: Login com usuário válido
    Dado que existe um usuário ativo cadastrado no sistema
    Quando o usuário informa login e senha corretos
    Então o sistema deve autenticar o usuário
    E deve retornar o nome e o perfil de acesso

  @BDD-02
  Cenário: Login com senha incorreta
    Dado que existe um usuário ativo cadastrado no sistema
    Quando o usuário informa uma senha incorreta
    Então o sistema não deve autenticar o usuário
    E deve informar que as credenciais são inválidas