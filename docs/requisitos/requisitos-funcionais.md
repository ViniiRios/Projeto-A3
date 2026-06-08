# Requisitos Funcionais — Sistema de Monitoramento Epidemiológico VigiA-SUS

## 1. Visão geral

O VigiA-SUS é um sistema acadêmico de monitoramento epidemiológico desenvolvido para apoiar a organização, consulta e análise de dados territoriais, epidemiológicos, climáticos e entomológicos.

O sistema permite o acompanhamento de áreas monitoradas, consulta de indicadores de ovitrampas, visualização de dados regionais, autenticação por perfil de usuário, pré-validação de arquivos de insumos e execução de um motor preditivo de risco epidemiológico.

---

## 2. Perfis de usuário

| Perfil                 | Descrição                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Gestor de TI           | Perfil técnico/administrativo com acesso amplo ao sistema.                                                               |
| Gestor Epidemiológico  | Perfil de gestão em saúde, com acesso amplo às funcionalidades de análise e acompanhamento.                              |
| Analista de Dados      | Perfil voltado à análise e conferência de dados, com acesso a dashboard, consultas territoriais e importação de insumos. |
| Operador de Importação | Perfil responsável pela validação e conferência de arquivos de insumos.                                                  |
| Analista de Vigilância | Perfil voltado à consulta de áreas monitoradas, ovitrampas e dados de apoio à vigilância.                                |

---

## 3. Requisitos funcionais

| ID    | Requisito funcional                                                                                                                                                         | Prioridade | Status                        |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------------------------- |
| RF-01 | O sistema deve permitir autenticação de usuários por login e senha.                                                                                                         | Alta       | Implementado                  |
| RF-02 | O sistema deve controlar o acesso aos módulos conforme o perfil do usuário autenticado.                                                                                     | Alta       | Implementado                  |
| RF-03 | O sistema deve exibir um Dashboard Preditivo para análise de risco epidemiológico.                                                                                          | Alta       | Implementado                  |
| RF-04 | O sistema deve permitir informar temperatura média, pluviosidade, casos atuais, casos anteriores e população para executar a análise de risco.                              | Alta       | Implementado                  |
| RF-05 | O sistema deve calcular a taxa de incidência epidemiológica por 100 mil habitantes.                                                                                         | Alta       | Implementado                  |
| RF-06 | O sistema deve classificar o risco epidemiológico em níveis como risco baixo, risco moderado e alerta máximo.                                                               | Alta       | Implementado / Em refinamento |
| RF-07 | O sistema deve exibir dados regionais de casos e clima, incluindo casos de dengue, chikungunya, zika, total de casos, temperatura média, precipitação e população regional. | Média      | Implementado                  |
| RF-08 | O sistema deve listar áreas monitoradas cadastradas no banco de dados.                                                                                                      | Alta       | Implementado                  |
| RF-09 | O sistema deve permitir o cadastro de novas áreas monitoradas.                                                                                                              | Alta       | Implementado                  |
| RF-10 | O sistema deve gerar automaticamente o código da área monitorada durante o cadastro.                                                                                        | Média      | Implementado                  |
| RF-11 | O sistema deve permitir inativar áreas monitoradas sem removê-las fisicamente do banco de dados.                                                                            | Alta       | Implementado                  |
| RF-12 | O sistema deve permitir reativar áreas monitoradas inativas.                                                                                                                | Alta       | Implementado                  |
| RF-13 | O sistema deve permitir consultar indicadores de ovitrampas vinculados a uma área monitorada.                                                                               | Alta       | Implementado                  |
| RF-14 | O sistema deve exibir indicadores entomológicos, como total de armadilhas, armadilhas positivas, negativas e percentual de positividade.                                    | Média      | Implementado                  |
| RF-15 | O sistema deve permitir a pré-validação de arquivos CSV de insumos.                                                                                                         | Alta       | Implementado                  |
| RF-16 | O sistema deve verificar colunas esperadas, colunas encontradas, colunas faltantes, colunas extras e campos vazios nos arquivos CSV.                                        | Alta       | Implementado                  |
| RF-17 | O sistema deve permitir o download de modelos CSV para os tipos de insumo aceitos.                                                                                          | Média      | Implementado                  |
| RF-18 | O sistema deve registrar temporariamente o histórico de validações de insumos durante a sessão do usuário.                                                                  | Média      | Implementado                  |
| RF-19 | O sistema deve exibir uma tela informativa “Sobre o Projeto” com objetivo, versão, módulos e equipe.                                                                        | Baixa      | Implementado                  |
| RF-20 | O sistema deve integrar o backend Java ao serviço Python responsável pelo motor preditivo.                                                                                  | Alta       | Implementado / Em refinamento |
| RF-21 | O sistema deve persistir dados de áreas, ovitrampas, casos/clima e usuários em banco PostgreSQL.                                                                            | Alta       | Implementado                  |

---

## 4. Funcionalidades observáveis pelo usuário

As principais funcionalidades observáveis do sistema são:

1. Realizar login no sistema.
2. Acessar módulos conforme perfil de usuário.
3. Executar análise de risco epidemiológico no Dashboard Preditivo.
4. Visualizar dados regionais de casos e clima.
5. Listar áreas monitoradas.
6. Cadastrar nova área monitorada.
7. Inativar área monitorada.
8. Reativar área monitorada.
9. Consultar ovitrampas por área.
10. Visualizar indicadores entomológicos.
11. Validar arquivos CSV de insumos.
12. Baixar modelos CSV.
13. Consultar histórico temporário de validações.
14. Consultar informações gerais do projeto.

---

## 5. Regras de negócio

| ID    | Regra de negócio              | Descrição                                                                                                      |
| ----- | ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| RN-01 | Cálculo da taxa de incidência | A taxa de incidência deve ser calculada com base na fórmula: casos atuais × 100.000 / população.               |
| RN-02 | Classificação de risco        | O sistema deve classificar o risco epidemiológico em faixas, como risco baixo, risco moderado e alerta máximo. |
| RN-03 | Controle por perfil           | O acesso aos módulos deve variar conforme o perfil do usuário autenticado.                                     |
| RN-04 | Código automático de área     | O código da área deve ser gerado automaticamente pelo backend, evitando códigos manuais inconsistentes.        |
| RN-05 | Inativação sem exclusão       | Áreas monitoradas não devem ser removidas fisicamente do banco; devem ser marcadas como ativas ou inativas.    |
| RN-06 | Validação de insumos          | Arquivos CSV devem ser conferidos quanto à estrutura antes da carga oficial no banco de dados.                 |
| RN-07 | Integração preditiva          | A análise de risco deve utilizar integração entre backend Java e serviço Python de apoio preditivo.            |

---

## 6. Escopo do MVP

O MVP atual contempla:

* autenticação funcional com usuários persistidos no banco;
* controle básico de acesso por perfil;
* persistência em PostgreSQL;
* gestão de áreas monitoradas;
* consulta de ovitrampas;
* consulta de dados regionais;
* pré-validação de arquivos CSV;
* integração com serviço Python para apoio ao cálculo/classificação de risco;
* interface web em Streamlit.

Ficam como evolução futura:

* criptografia de senhas;
* autenticação com token;
* CRUD administrativo completo de usuários;
* persistência do histórico de importações;
* importação automática definitiva de CSV para o banco pela interface;
* ampliação da base histórica para melhoria do modelo preditivo;
* dashboards cartográficos/georreferenciados.
