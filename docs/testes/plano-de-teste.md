# 🧪✅ Plano de Teste — VigiA-SUS

### 📋 Convenções e status

| Item            | Padrão ✅                                                                                        |
| --------------- | ----------------------------------------------------------------------------------------------- |
| 🏷️ ID do teste | **RT-XX** para roteiros manuais, **UT-XX** para testes unitários e **BDD-XX** para cenários BDD |
| 📌 Status       | 🟡 Planejado • 🔵 Em execução • 🟢 Passou • 🔴 Falhou • ⚫ Bloqueado                             |
| ⭐ Prioridade    | 🔥 Alta • ⚠️ Média • 🟦 Baixa                                                                   |
| 📎 Evidência    | Print / log / vídeo / link do PR/Issue                                                          |

---

### 🆔📖 Identificação e contexto

| Campo                                       | Preencher ✍️                                                                                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🧩 Nome do projeto                          | VigiA-SUS — Sistema de Monitoramento Epidemiológico                                                                                                                                                                                                                   |
| 📝 Objetivo do sistema (resumo)             | Apoiar o monitoramento epidemiológico por meio da organização, consulta e análise de dados territoriais, climáticos, epidemiológicos e entomológicos, permitindo acompanhar áreas monitoradas, consultar ovitrampas, validar insumos e classificar cenários de risco. |
| 🎯 Público-alvo                             | Gestores epidemiológicos, analistas de vigilância, analistas de dados, operadores de importação e responsáveis técnicos pelo sistema.                                                                                                                                 |
| 💻 Plataforma/Tipo (console/web/mobile/API) | Aplicação web/protótipo em Streamlit, backend API REST em Java/Spring Boot, serviço Python para motor preditivo e banco PostgreSQL.                                                                                                                                   |
| 🔗 Repositório                              | GitHub — Projeto-A3                                                                                                                                                                                                                                                   |
| 👥 Time/Grupo                               | Daniela Teixeira Abreu, Vinícius Raphael Rios, Matheus Felipe Lopes, Nátali Isaltino Gomes e Marcela Maria Barbosa                                                                                                                                                    |

---

### 🎯🧪 Objetivo do teste

| Item                                 | Descrição 🗒️                                                                                                                                                                                                                                                                       |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅ Objetivo geral                     | Verificar se as funcionalidades principais do VigiA-SUS estão operando conforme os requisitos definidos, cobrindo autenticação, controle de acesso, gestão territorial, cálculo/classificação de risco, consulta de ovitrampas, dados regionais, importação e validação de insumos. |
| 📊 Metas de cobertura (se aplicável) | Cobrir regras e serviços principais com testes unitários; automatizar cenários BDD; executar roteiros manuais dos fluxos principais; registrar evidências dos fluxos positivos, validações/erros e controle de acesso; realizar teste de usabilidade com 3 participantes.           |

---

### 📦📌 Escopo

| Categoria                               | ✅ Em escopo                                                                                                                                                                                                                                      | 🚫 Fora de escopo                                                                                                                  |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| 🧩 Funcionalidades                      | Login, controle de perfil, dashboard preditivo, cálculo de risco, listagem de áreas, formulário de cadastro de área, tela de manutenção, consulta de ovitrampas, dados regionais, tela de importação, regras dos insumos e tela Sobre o Projeto. | Funcionalidades futuras não implementadas, como CRUD completo de usuários, recuperação de senha e mapas georreferenciados.         |
| 🧠 Regras de negócio                    | Taxa de incidência, classificação de risco, geração automática de código de área, manutenção de status de área, controle por perfil e validação estrutural de CSV.                                                                               | Regras avançadas de segurança, autenticação com token e importação automática definitiva dos arquivos para o banco pela interface. |
| 🔌 Integrações                          | Frontend Streamlit com backend Java, backend Java com PostgreSQL e backend Java com serviço Python.                                                                                                                                              | Integrações externas em produção, APIs públicas em tempo real e deploy em nuvem.                                                   |
| 🗃️ Dados                               | Áreas monitoradas, ovitrampas, casos e clima, usuários e arquivos CSV de insumos.                                                                                                                                                                | Bases históricas ampliadas ainda não consolidadas e dados externos não tratados.                                                   |
| 🧑‍💻 Não-funcionais (usabilidade etc.) | Execução local, organização em camadas, usabilidade básica, documentação, rastreabilidade e testes automatizados/manuais.                                                                                                                        | Testes de carga, segurança avançada, disponibilidade em produção e auditoria completa de acessos.                                  |

---

### 🧰🖥️ Ambiente e ferramentas

| Item                            | Especificação ⚙️                                                         |
| ------------------------------- | ------------------------------------------------------------------------ |
| 🖥️ SO                          | Windows                                                                  |
| ☕ Linguagem/Runtime             | Java 17+, Python 3, Streamlit                                            |
| 🧑‍💻 IDE                       | Visual Studio Code                                                       |
| 🧱 Build                        | Maven / Maven Wrapper (`mvnw.cmd`)                                       |
| ✅ Framework de testes unitários | JUnit 5, Mockito                                                         |
| 🥒 BDD (se houver)              | Cucumber com Gherkin                                                     |
| 🤖 CI (se houver)               | Não configurado nesta versão MVP                                         |
| 🗄️ Banco/Dados (se houver)     | PostgreSQL, DBeaver, arquivos CSV tratados e dados importados localmente |
| 🌐 Teste de API                 | Postman                                                                  |
| 🖥️ Interface                   | Streamlit em ambiente local                                              |

---

### 🧪🧱 Estratégia de testes (por tipo)

| Tipo de teste         | 🎯 Objetivo                                                                 | 📌 Escopo                                                                                             | 🛠️ Ferramenta                                    | 👤 Responsável                   | 📎 Saída/Evidência                                                   |
| --------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------- |
| ✅ Unitário            | Verificar regras e serviços de forma isolada.                               | Serviços de área, risco, integração IA e regras de cadastro/manutenção.                               | JUnit 5, Mockito, Maven                           | Equipe de desenvolvimento        | Prints/logs em `docs/evidencias-finais/unitarios/` com BUILD SUCCESS |
| 🌐 Sistema/End-to-End | Verificar fluxos completos da aplicação em ambiente local.                  | Login, dashboard, gestão territorial, ovitrampas, dados regionais, importação e tela Sobre o Projeto. | Streamlit, Postman, DBeaver                       | Equipe de desenvolvimento/testes | Prints da interface em `docs/evidencias-finais/manuais/`             |
| 🥒 BDD                | Validar comportamento esperado dos fluxos essenciais com linguagem Gherkin. | Login, áreas, manutenção de área, risco epidemiológico e ovitrampas.                                  | Cucumber, Gherkin, Maven                          | Equipe de desenvolvimento/testes | Relatório Cucumber e prints em `docs/evidencias-finais/unitarios/`   |
| 🧑‍💻 Usabilidade     | Avaliar clareza, facilidade e fluidez da interface com usuários.            | Login, dashboard, gestão territorial, importação de insumos e consulta de informações.                | Observação guiada, questionário e registro manual | Equipe do projeto                | Documento e evidências em `docs/evidencias-finais/usabilidade/`      |

---

### 🧷🧭 Rastreabilidade (Requisitos x Testes)

| ID Req | Requisito/Funcionalidade                      | ⭐ Prioridade | 🔗 Fonte (Issue/PR) | 🧪 IDs de testes (UT/BDD/RT)                 | 📌 Status |
| ------ | --------------------------------------------- | ------------ | ------------------- | -------------------------------------------- | --------- |
| RF-01  | Autenticação de usuários por login e senha    | 🔥 Alta      | A preencher         | BDD-01, BDD-02, RT-01, RT-14                 | 🟢 Passou |
| RF-02  | Controle de acesso por perfil de usuário      | 🔥 Alta      | A preencher         | RT-02                                        | 🟢 Passou |
| RF-03  | Dashboard Preditivo                           | 🔥 Alta      | A preencher         | RT-03, RT-12                                 | 🟢 Passou |
| RF-04  | Entrada de dados epidemiológicos e climáticos | 🔥 Alta      | A preencher         | BDD-07, BDD-08, BDD-09, RT-03, RT-12         | 🟢 Passou |
| RF-05  | Cálculo da taxa de incidência                 | 🔥 Alta      | A preencher         | UT-03, BDD-07, BDD-08, BDD-09, RT-03, RT-12  | 🟢 Passou |
| RF-06  | Classificação de risco epidemiológico         | 🔥 Alta      | A preencher         | UT-03, BDD-07, BDD-08, BDD-09, RT-03, RT-12  | 🟢 Passou |
| RF-07  | Exibição de dados regionais de casos e clima  | ⚠️ Média     | A preencher         | RT-04                                        | 🟢 Passou |
| RF-08  | Listagem de áreas monitoradas                 | 🔥 Alta      | A preencher         | UT-01, BDD-04, RT-05                         | 🟢 Passou |
| RF-09  | Cadastro de áreas monitoradas                 | 🔥 Alta      | A preencher         | UT-01, BDD-03, RT-06                         | 🟢 Passou |
| RF-10  | Geração automática de código da área          | ⚠️ Média     | A preencher         | UT-01, BDD-03, RT-06                         | 🟢 Passou |
| RF-11  | Inativação de área monitorada                 | 🔥 Alta      | A preencher         | UT-01, BDD-05, RT-07                         | 🟢 Passou |
| RF-12  | Reativação de área monitorada                 | 🔥 Alta      | A preencher         | UT-01, BDD-06, RT-07                         | 🟢 Passou |
| RF-13  | Consulta de ovitrampas por área               | 🔥 Alta      | A preencher         | BDD-10, BDD-11, RT-08                        | 🟢 Passou |
| RF-14  | Exibição de indicadores entomológicos         | ⚠️ Média     | A preencher         | BDD-10, RT-08                                | 🟢 Passou |
| RF-15  | Pré-validação de arquivos CSV de insumos      | 🔥 Alta      | A preencher         | RT-09, RT-10, RT-13                          | 🟢 Passou |
| RF-16  | Verificação de colunas e campos vazios em CSV | 🔥 Alta      | A preencher         | RT-09, RT-10, RT-13                          | 🟢 Passou |
| RF-17  | Download de modelos CSV                       | ⚠️ Média     | A preencher         | RT-09                                        | 🟢 Passou |
| RF-18  | Histórico temporário de validações            | ⚠️ Média     | A preencher         | RT-10                                        | 🟢 Passou |
| RF-19  | Tela Sobre o Projeto                          | 🟦 Baixa     | A preencher         | RT-11                                        | 🟢 Passou |
| RF-20  | Integração Java com serviço Python            | 🔥 Alta      | A preencher         | UT-04, RT-03, RT-12                          | 🟢 Passou |
| RF-21  | Persistência em PostgreSQL                    | 🔥 Alta      | A preencher         | RT-05, RT-08, BDD-03, BDD-04, BDD-05, BDD-06 | 🟢 Passou |

> 🏷️ Convenção utilizada:
>
> * ✅ **UT-XX**: teste unitário automatizado;
> * 🥒 **BDD-XX**: cenário BDD automatizado;
> * 📝 **RT-XX**: roteiro manual.

---

### 🧾🧪 Casos de teste executados (resumo)

| ID     | 🧪 Tipo    | 🏷️ Título                                          | 🔐 Pré-condição                         | 📥 Entrada                              | ✅ Resultado esperado                                       | ⭐ Prioridade | 🤖 Automatizado? |
| ------ | ---------- | --------------------------------------------------- | --------------------------------------- | --------------------------------------- | ---------------------------------------------------------- | ------------ | ---------------- |
| UT-01  | ✅ Unitário | Testes do serviço de cadastro e manutenção de áreas | Projeto compilando                      | Dados simulados de área                 | Cadastro, listagem, geração de código e status funcionando | 🔥 Alta      | Sim              |
| UT-02  | ✅ Unitário | Teste do serviço de predição de área                | IAClient mockado                        | Requisição simulada                     | Retornar risco e taxa esperados                            | 🔥 Alta      | Sim              |
| UT-03  | ✅ Unitário | Teste do serviço epidemiológico                     | Dados epidemiológicos simulados         | Casos, população e variáveis climáticas | Calcular/classificar risco conforme regra                  | 🔥 Alta      | Sim              |
| UT-04  | ✅ Unitário | Teste de integração com IA                          | Serviço Python simulado/mockado         | Payload de predição                     | Retornar resposta válida da integração                     | 🔥 Alta      | Sim              |
| BDD-01 | 🥒 BDD     | Login com usuário válido                            | Usuário ativo cadastrado                | Login e senha corretos                  | Usuário autenticado com nome e perfil                      | 🔥 Alta      | Sim              |
| BDD-02 | 🥒 BDD     | Login com senha incorreta                           | Usuário ativo cadastrado                | Senha incorreta                         | Usuário não autenticado                                    | 🔥 Alta      | Sim              |
| BDD-03 | 🥒 BDD     | Cadastro de área monitorada                         | Backend em execução                     | Dados válidos de área                   | Área salva com código automático e status ATIVA            | 🔥 Alta      | Sim              |
| BDD-04 | 🥒 BDD     | Listagem de áreas monitoradas                       | Áreas cadastradas                       | Solicitação de listagem                 | Lista de áreas retornada com campos esperados              | 🔥 Alta      | Sim              |
| BDD-05 | 🥒 BDD     | Inativação de área                                  | Área com status ATIVA                   | Solicitação de inativação               | Área com status INATIVA sem exclusão                       | 🔥 Alta      | Sim              |
| BDD-06 | 🥒 BDD     | Reativação de área                                  | Área com status INATIVA                 | Solicitação de reativação               | Área com status ATIVA novamente                            | 🔥 Alta      | Sim              |
| BDD-07 | 🥒 BDD     | Classificar risco baixo                             | Dados de baixa incidência               | Poucos casos e população alta           | Resultado RISCO BAIXO                                      | 🔥 Alta      | Sim              |
| BDD-08 | 🥒 BDD     | Classificar risco moderado                          | Dados de incidência intermediária       | Casos intermediários e população        | Resultado RISCO MODERADO                                   | 🔥 Alta      | Sim              |
| BDD-09 | 🥒 BDD     | Classificar alerta máximo                           | Dados de alta incidência                | Muitos casos e população                | Resultado ALERTA MÁXIMO                                    | 🔥 Alta      | Sim              |
| BDD-10 | 🥒 BDD     | Consultar ovitrampas de área existente              | Área com ovitrampas cadastradas         | Código da área                          | Indicadores entomológicos retornados                       | ⚠️ Média     | Sim              |
| BDD-11 | 🥒 BDD     | Consultar ovitrampas sem registros                  | Área sem ovitrampas                     | Código da área                          | Lista vazia sem erro                                       | ⚠️ Média     | Sim              |
| RT-01  | 📝 Manual  | Login válido no sistema                             | Backend e Streamlit em execução         | Usuário e senha válidos                 | Acesso liberado conforme perfil                            | 🔥 Alta      | Não              |
| RT-02  | 📝 Manual  | Controle de acesso por perfil                       | Usuários cadastrados                    | Login com diferentes perfis             | Módulos exibidos conforme perfil                           | 🔥 Alta      | Não              |
| RT-03  | 📝 Manual  | Cálculo de risco no Dashboard                       | Backend, Python e Streamlit em execução | Dados epidemiológicos e climáticos      | Exibir classificação de risco e taxa                       | 🔥 Alta      | Não              |
| RT-04  | 📝 Manual  | Consulta de dados regionais                         | Casos/clima cadastrados no banco        | Acesso à aba Dados Regionais            | Exibir dados regionais corretamente                        | ⚠️ Média     | Não              |
| RT-05  | 📝 Manual  | Listagem de áreas monitoradas                       | Áreas cadastradas no banco              | Acesso à Gestão Territorial             | Exibir lista de áreas e métricas                           | 🔥 Alta      | Não              |
| RT-06  | 📝 Manual  | Formulário de cadastro de área monitorada           | Perfil com acesso completo              | Acesso à aba Nova Área                  | Formulário de cadastro disponível com campos obrigatórios  | 🔥 Alta      | Não              |
| RT-07  | 📝 Manual  | Tela de manutenção de área monitorada               | Área existente no banco                 | Área selecionada para manutenção        | Exibir status atual e botões de inativar/reativar área     | 🔥 Alta      | Não              |
| RT-08  | 📝 Manual  | Consulta de ovitrampas por área                     | Dados de ovitrampas importados          | Área selecionada no sistema             | Exibir indicadores da área                                 | ⚠️ Média     | Não              |
| RT-09  | 📝 Manual  | Tela de validação de CSV e modelo de insumo         | Usuário com acesso à importação         | Tipo de insumo selecionado              | Exibir modelo CSV, upload e mensagem de arquivo ausente    | ⚠️ Média     | Não              |
| RT-10  | 📝 Manual  | Ausência de arquivo e histórico de importações      | Usuário com acesso à importação         | Nenhum arquivo anexado                  | Informar ausência de arquivo e histórico da sessão         | ⚠️ Média     | Não              |
| RT-11  | 📝 Manual  | Consulta da tela Sobre o Projeto                    | Usuário autenticado                     | Acesso ao módulo Sobre o Projeto        | Exibir objetivo, versão, módulos e equipe                  | 🟦 Baixa     | Não              |
| RT-12  | 📝 Manual  | Validação de cenário no cálculo de risco            | Backend, Python e Streamlit em execução | Dados epidemiológicos e climáticos      | Exibir classificação de risco e dados calculados           | 🔥 Alta      | Não              |
| RT-13  | 📝 Manual  | Regras dos insumos                                  | Usuário com acesso à importação         | Acesso à aba Regras dos Insumos         | Exibir regras e recomendações para arquivos CSV            | ⚠️ Média     | Não              |
| RT-14  | 📝 Manual  | Login com credenciais inválidas                     | Backend e Streamlit em execução         | Usuário e senha inválidos               | Bloquear acesso e exibir mensagem de erro                  | ⚠️ Média     | Não              |

---

### 🗃️🧪 Dados de teste

| ID    | 🧺 Conjunto                 | 📝 Descrição                                                    | 🧪 Como criar                                                            | 📍 Onde armazenar                 | 💡 Observações                                                      |
| ----- | --------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------------- |
| DT-01 | Usuários de teste           | Usuários com perfis diferentes para validar login e permissões. | Inseridos na tabela `usuarios` do PostgreSQL.                            | Banco PostgreSQL local            | Ex.: Daniela, Vinícius, Matheus, Nátali e Marcela.                  |
| DT-02 | Áreas monitoradas           | Base territorial de áreas monitoradas.                          | Importação via CSV/DBeaver ou cadastro via sistema.                      | Tabela `areas`                    | Deve preservar `codigo_area` com zeros à esquerda.                  |
| DT-03 | Ovitrampas                  | Indicadores entomológicos por área.                             | Importação da planilha de ovitrampas.                                    | Tabela `ovitrampas`               | Usada na consulta por código de área.                               |
| DT-04 | Casos e clima               | Dados epidemiológicos e climáticos por regional.                | Importação da planilha `casos_clima.csv`.                                | Tabela `casos_clima`              | Exibida na aba Dados Regionais.                                     |
| DT-05 | Modelo CSV de insumos       | Modelo CSV disponibilizado pela tela de importação.             | Selecionar o tipo de insumo e usar o botão de download do modelo.        | `docs/evidencias-finais/manuais/` | Usado para validar a disponibilidade do modelo e da tela de upload. |
| DT-06 | Ausência de arquivo anexado | Cenário sem upload de arquivo na tela de validação.             | Acessar a tela de validação sem anexar arquivo.                          | `docs/evidencias-finais/manuais/` | Usado para validar mensagem de ausência de arquivo.                 |
| DT-07 | Dados de cenário de risco   | Dados epidemiológicos e climáticos usados no Dashboard.         | Informar temperatura, pluviosidade, casos, casos anteriores e população. | Registro no roteiro/evidência     | Usado para cálculo e classificação de risco.                        |

---

### 📌 Observações

Este plano de teste representa a versão final de validação do MVP VigiA-SUS.

Os testes automatizados unitários e BDD foram executados via Maven, com evidências registradas na pasta `docs/evidencias-finais/unitarios/`.

Os testes manuais foram executados a partir da interface Streamlit, cobrindo login, controle de acesso por perfil, dashboard preditivo, dados regionais, gestão territorial, consulta de ovitrampas, formulário de cadastro de áreas, tela de manutenção, central de importação, regras dos insumos e tela Sobre o Projeto. As evidências foram registradas na pasta `docs/evidencias-finais/manuais/`.

O teste de usabilidade foi previsto para validação com 3 participantes, com registro próprio na pasta `docs/evidencias-finais/usabilidade/`.
