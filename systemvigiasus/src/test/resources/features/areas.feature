# language: pt

Funcionalidade: Gestão de áreas monitoradas
  Como gestor do sistema
  Quero cadastrar e consultar áreas monitoradas
  Para manter a base territorial do monitoramento epidemiológico atualizada

  @BDD-03
  Cenário: Cadastrar uma nova área monitorada com dados válidos
    Dado que o backend está em execução
    E existem áreas monitoradas cadastradas no banco
    Quando uma nova área é cadastrada com nome, unidade de saúde, bairro, regional e população
    Então o sistema deve salvar a área no banco de dados
    E deve gerar automaticamente um código para a área
    E deve cadastrar a área com status ATIVA

  @BDD-04
  Cenário: Listar áreas monitoradas cadastradas
    Dado que existem áreas monitoradas cadastradas no banco
    Quando o usuário solicita a listagem de áreas
    Então o sistema deve retornar a lista de áreas cadastradas
    E cada área deve apresentar código, bairro, regional, unidade de saúde, população e status