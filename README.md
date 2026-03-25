# Sistema de Monitoramento Epidemiológico

## 📌 Visão Geral

O sistema consiste em uma aplicação web desenvolvida em Java com o objetivo de apoiar o monitoramento epidemiológico e a gestão de risco em saúde pública. A solução permite centralizar e organizar dados relacionados a áreas monitoradas, como registros de armadilhas, quantidade de casos e informações relevantes para análise.

A principal proposta do sistema é facilitar a visualização e o acompanhamento de regiões com maior risco epidemiológico, permitindo que usuários consultem dados, identifiquem padrões e tenham uma visão mais clara da situação de cada área.

O sistema é voltado para profissionais e gestores da área da saúde, oferecendo uma ferramenta digital para apoio à tomada de decisão, organização de informações e análise de dados de forma mais estruturada.

Como diferencial, o sistema permite a aplicação de uma lógica de cálculo de risco baseada nos dados coletados, possibilitando classificar automaticamente as áreas em níveis como baixo, moderado ou alto risco.

---

## 🏗️ Arquitetura Mínima

A aplicação segue uma arquitetura simples baseada em separação de responsabilidades, utilizando o padrão de desenvolvimento em camadas.

### 🔹 Backend

O backend é desenvolvido em Java utilizando o framework Spring Boot. Ele é responsável por:

- Gerenciar as regras de negócio do sistema  
- Organizar e estruturar os dados  
- Expor endpoints REST para acesso às informações  

A aplicação possui controladores responsáveis por receber requisições HTTP e retornar respostas no formato JSON.

---

### 🔹 Estrutura de Dados

Os dados do sistema são representados por classes Java (modelos), como a entidade de área, que contém informações como:

- Identificador da área  
- Nome da região  
- Unidade de saúde associada  
- Quantidade de armadilhas  
- Quantidade de resultados positivos  
- Nível de risco  

Nesta fase inicial, os dados são simulados em memória, sem persistência em banco de dados.

---

### 🔹 API REST

A comunicação com o sistema é feita por meio de endpoints REST. Um exemplo implementado é:

- `GET /areas` → retorna a lista de áreas monitoradas  

As respostas são fornecidas em formato JSON, permitindo fácil integração com futuras interfaces.

---

### 🔹 Front-end (Planejado)

A interface do sistema será desenvolvida posteriormente como uma aplicação web, com o objetivo de permitir:

- Visualização dos dados de forma organizada  
- Interação com filtros e consultas  
- Apresentação dos níveis de risco  

---

### 🔹 Banco de Dados (Planejado)

Está prevista a integração com um banco de dados relacional, que permitirá:

- Persistência dos dados  
- Armazenamento estruturado das informações  
- Suporte a consultas mais avançadas  

---

## 🚀 Status do Projeto

Atualmente, o sistema se encontra em fase inicial de desenvolvimento (Sprint 0), já possuindo:

- Estrutura base do backend configurada  
- Primeiros endpoints funcionando  
- Representação inicial dos dados  

Essa etapa tem como objetivo validar o funcionamento da aplicação e preparar a base para as próximas evoluções.


---
## 👨‍💻 Integrantes

* Daniela Teixeira Abreu – 4231923259
* Marcela Maria Barbosa - 422222661
* Matheus Felipe Lopes da Silva - 4231925981
* Nátali Isaltino Gomes - 4231925815
* Vinícius Raphael Rios de Lima - 42321398
