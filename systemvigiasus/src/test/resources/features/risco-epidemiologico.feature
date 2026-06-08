# language: pt

Funcionalidade: Cálculo de risco epidemiológico
  Como gestor epidemiológico
  Quero informar dados epidemiológicos e climáticos
  Para obter uma classificação de risco da área analisada

  @BDD-07
  Cenário: Classificar risco baixo
    Dado que o usuário informa poucos casos em relação à população
    Quando o sistema calcula a taxa de incidência
    Então o resultado deve indicar RISCO BAIXO

  @BDD-08
  Cenário: Classificar risco moderado
    Dado que o usuário informa quantidade intermediária de casos em relação à população
    Quando o sistema calcula a taxa de incidência
    Então o resultado deve indicar RISCO MODERADO

  @BDD-09
  Cenário: Classificar alerta máximo
    Dado que o usuário informa muitos casos em relação à população
    Quando o sistema calcula a taxa de incidência
    Então o resultado deve indicar ALERTA MÁXIMO