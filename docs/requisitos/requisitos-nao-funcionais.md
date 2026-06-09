# Requisitos Não Funcionais — Sistema de Monitoramento Epidemiológico VigiA-SUS

## 1. Visão geral

Este documento apresenta os requisitos não funcionais do VigiA-SUS, relacionados à qualidade, desempenho, usabilidade, segurança, manutenibilidade, compatibilidade e rastreabilidade do sistema.

---

## 2. Requisitos não funcionais

| ID     | Requisito não funcional                                                                                                               | Prioridade | Status                    |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------- |
| RNF-01 | O sistema deve utilizar Java com Spring Boot no backend.                                                                              | Alta       | Implementado              |
| RNF-02 | O projeto backend deve utilizar Maven como ferramenta de build.                                                                       | Alta       | Implementado              |
| RNF-03 | O sistema deve utilizar PostgreSQL para persistência dos dados principais.                                                            | Alta       | Implementado              |
| RNF-04 | O sistema deve possuir arquitetura organizada em camadas/pacotes, separando domínio, serviços, persistência/adaptações e entrada/API. | Alta       | Implementado              |
| RNF-05 | O sistema deve possuir interface web/protótipo funcional em Streamlit.                                                                | Alta       | Implementado              |
| RNF-06 | O sistema deve possuir integração entre frontend, backend Java, banco PostgreSQL e serviço Python.                                    | Alta       | Implementado              |
| RNF-07 | O sistema deve possuir testes unitários para regras e serviços principais.                                                            | Alta       | Implementado              |
| RNF-08 | O projeto deve possuir cenários BDD em Gherkin automatizados com Cucumber ou ferramenta equivalente.                                  | Alta       | Implementado              |
| RNF-09 | O sistema deve permitir execução local em ambiente de desenvolvimento.                                                                | Alta       | Implementado              |
| RNF-10 | O sistema deve apresentar mensagens de erro claras quando backend, banco ou serviço Python estiverem indisponíveis.                   | Média      | Parcialmente implementado |
| RNF-11 | O sistema deve ter README atualizado com instruções de execução, tecnologias, funcionalidades e testes.                               | Alta       | Implementado              |
| RNF-12 | O projeto deve manter histórico de commits frequentes e descritivos no GitHub.                                                        | Alta       | Implementado              |
| RNF-13 | As entregas devem ser rastreáveis por issues, commits, pull requests e evidências.                                                    | Alta       | Implementado              |
| RNF-14 | O sistema deve apresentar interface compreensível para usuários não técnicos da área de saúde.                                        | Média      | Em refinamento            |
| RNF-15 | As telas devem possuir organização visual suficiente para demonstração do MVP.                                                        | Média      | Em refinamento            |
| RNF-16 | O sistema deve preservar dados de áreas monitoradas no banco mesmo quando elas forem inativadas.                                      | Alta       | Implementado              |
| RNF-17 | O sistema deve validar arquivos CSV antes da carga oficial para reduzir inconsistências nos dados.                                    | Alta       | Implementado              |
| RNF-18 | O sistema deve separar funcionalidades reais de funcionalidades demonstrativas/MVP na documentação.                                   | Alta       | Implementado              |
| RNF-19 | O sistema deve permitir execução dos testes automatizados pelo Maven.                                                                 | Alta       | Implementado              |
| RNF-20 | O projeto deve possuir documentação de testes, incluindo plano de teste, roteiros manuais, BDD e usabilidade.                         | Alta       | Parcialmente implementado |