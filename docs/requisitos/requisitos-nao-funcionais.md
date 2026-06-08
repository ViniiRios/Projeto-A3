# Requisitos Não Funcionais — Sistema de Monitoramento Epidemiológico VigiA-SUS

## 1. Visão geral

Este documento apresenta os requisitos não funcionais do VigiA-SUS, considerando qualidade, desempenho, usabilidade, manutenibilidade, segurança, compatibilidade e rastreabilidade do sistema.

---

## 2. Requisitos não funcionais

| ID     | Requisito não funcional                                                                                                               | Prioridade | Status                     |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------------------------- |
| RNF-01 | O sistema deve utilizar Java com Spring Boot no backend.                                                                              | Alta       | Implementado               |
| RNF-02 | O projeto backend deve utilizar Maven como ferramenta de build.                                                                       | Alta       | Implementado               |
| RNF-03 | O sistema deve utilizar PostgreSQL para persistência dos dados principais.                                                            | Alta       | Implementado               |
| RNF-04 | O sistema deve possuir arquitetura organizada em camadas/pacotes, separando domínio, serviços, persistência/adaptações e entrada/API. | Alta       | Implementado               |
| RNF-05 | O sistema deve possuir interface web/protótipo funcional em Streamlit.                                                                | Alta       | Implementado               |
| RNF-06 | O sistema deve possuir integração entre frontend, backend Java, banco PostgreSQL e serviço Python.                                    | Alta       | Implementado               |
| RNF-07 | O sistema deve possuir testes unitários para regras e serviços principais.                                                            | Alta       | Implementado / Em expansão |
| RNF-08 | O projeto deve possuir cenários BDD em Gherkin automatizados com Cucumber ou ferramenta equivalente.                                  | Alta       | Pendente                   |
| RNF-09 | O sistema deve permitir execução local em ambiente de desenvolvimento.                                                                | Alta       | Implementado               |
| RNF-10 | O sistema deve apresentar mensagens de erro claras quando backend, banco ou serviço Python estiverem indisponíveis.                   | Média      | Parcialmente implementado  |
| RNF-11 | O sistema deve ter README atualizado com instruções de execução, tecnologias, funcionalidades e testes.                               | Alta       | Em atualização             |
| RNF-12 | O projeto deve manter histórico de commits frequentes e descritivos no GitHub.                                                        | Alta       | Implementado               |
| RNF-13 | As entregas devem ser rastreáveis por issues, commits, pull requests e evidências.                                                    | Alta       | Em organização             |
| RNF-14 | O sistema deve apresentar interface compreensível para usuários não técnicos da área de saúde.                                        | Média      | Em refinamento             |
| RNF-15 | As telas devem possuir organização visual suficiente para demonstração do MVP.                                                        | Média      | Em refinamento             |
| RNF-16 | O sistema deve preservar dados de áreas monitoradas no banco mesmo quando elas forem inativadas.                                      | Alta       | Implementado               |
| RNF-17 | O sistema deve validar arquivos CSV antes da carga oficial para reduzir inconsistências nos dados.                                    | Alta       | Implementado               |
| RNF-18 | O sistema deve separar funcionalidades reais de funcionalidades demonstrativas/MVP na documentação.                                   | Alta       | Em atualização             |
| RNF-19 | O sistema deve permitir execução dos testes automatizados pelo Maven.                                                                 | Alta       | Implementado / Em expansão |
| RNF-20 | O projeto deve possuir documentação de testes, incluindo plano de teste, roteiros manuais, BDD e usabilidade.                         | Alta       | Em elaboração              |

---

## 3. Qualidade e manutenibilidade

O sistema deve manter organização de código em camadas, evitando concentrar lógica de negócio diretamente na interface.

A estrutura principal do backend deve separar:

* entidades e regras de domínio;
* repositórios/persistência;
* serviços/casos de uso;
* controladores/endpoints;
* DTOs de entrada e saída;
* clientes de integração externa.

Essa separação facilita manutenção, testes e evolução do sistema.

---

## 4. Usabilidade

A interface deve ser compreensível para usuários envolvidos em saúde pública e vigilância epidemiológica.

A navegação deve permitir acesso claro aos módulos principais:

* Dashboard Preditivo;
* Gestão Territorial;
* Importação de Insumos;
* Sobre o Projeto.

Os formulários devem apresentar campos compreensíveis e mensagens de feedback após ações como cadastro, validação de arquivo e execução do cálculo de risco.

---

## 5. Segurança

O sistema possui controle básico de autenticação e perfil de acesso.

Na versão MVP:

* usuários são persistidos no banco;
* o login é validado pelo backend;
* o frontend libera módulos conforme perfil;
* usuários inativos ou credenciais inválidas não devem acessar o sistema.

Limitações conhecidas do MVP:

* senhas ainda não possuem hash criptográfico;
* não há autenticação por token JWT;
* não há recuperação de senha;
* não há painel completo de administração de usuários.

Essas limitações devem ser tratadas como evolução futura.

---

## 6. Desempenho

Por se tratar de MVP acadêmico executado localmente, o sistema deve responder adequadamente para bases pequenas e médias utilizadas na demonstração.

As principais consultas esperadas são:

* listagem de áreas monitoradas;
* busca de áreas por ID;
* consulta de ovitrampas por área;
* listagem de casos e clima;
* validação de arquivos CSV;
* cálculo/classificação de risco.

---

## 7. Compatibilidade e ambiente

O sistema deve rodar localmente com:

* Java/Spring Boot;
* Maven;
* PostgreSQL;
* Python;
* Streamlit;
* navegador web;
* DBeaver/Postman como ferramentas de apoio e validação.

A execução completa exige três partes:

1. backend Java/Spring Boot;
2. serviço Python do motor preditivo;
3. frontend Streamlit.

---

## 8. Rastreabilidade

O desenvolvimento deve manter rastreabilidade entre:

* requisitos;
* issues;
* commits;
* pull requests;
* testes;
* evidências.

Essa rastreabilidade apoia a avaliação do processo Scrum, qualidade de software e versionamento do projeto.
