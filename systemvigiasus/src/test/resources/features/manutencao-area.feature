# language: pt

Funcionalidade: Manutenção de áreas monitoradas
  Como gestor do sistema
  Quero inativar e reativar áreas monitoradas
  Para controlar quais áreas participam do monitoramento ativo sem excluir dados históricos

  @BDD-05
  Cenário: Inativar uma área monitorada existente
    Dado que existe uma área monitorada com status ATIVA
    Quando o usuário solicita a inativação dessa área
    Então o sistema deve alterar o status da área para INATIVA
    E a área deve continuar cadastrada no banco de dados

  @BDD-06
  Cenário: Reativar uma área monitorada existente
    Dado que existe uma área monitorada com status INATIVA
    Quando o usuário solicita a reativação dessa área
    Então o sistema deve alterar o status da área para ATIVA
    E a área deve continuar disponível para consulta