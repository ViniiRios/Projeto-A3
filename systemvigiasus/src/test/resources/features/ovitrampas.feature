# language: pt

Funcionalidade: Consulta de ovitrampas por área
  Como analista de vigilância
  Quero consultar indicadores de ovitrampas por área monitorada
  Para acompanhar sinais entomológicos relacionados ao risco epidemiológico

  @BDD-10
  Cenário: Consultar ovitrampas de uma área existente
    Dado que existe uma área monitorada com código cadastrado
    E existem dados de ovitrampas vinculados a essa área
    Quando o usuário consulta as ovitrampas pelo código da área
    Então o sistema deve retornar os indicadores da área
    E deve exibir total de armadilhas, positivas, negativas e percentual de positividade

  @BDD-11
  Cenário: Consultar ovitrampas de uma área sem registros
    Dado que existe uma área monitorada sem registros de ovitrampas
    Quando o usuário consulta as ovitrampas pelo código da área
    Então o sistema deve retornar uma lista vazia
    E não deve apresentar erro na consulta