# Sistema de Monitoramento Epidemiológico

## 📌 Visão Geral

O sistema consiste em uma aplicação web desenvolvida em Java com o objetivo de apoiar o monitoramento epidemiológico e a gestão de risco em saúde pública. A solução permite centralizar e organizar dados relacionados a áreas monitoradas, como registros epidemiológicos, dados climáticos, informações territoriais e indicadores utilizados na análise de risco.

A principal proposta do sistema é facilitar a visualização e o acompanhamento de regiões com maior risco epidemiológico, permitindo que usuários consultem dados, identifiquem padrões e tenham uma visão mais clara da situação de cada área monitorada.

O sistema é voltado para profissionais e gestores da área da saúde, oferecendo uma ferramenta digital para apoio à tomada de decisão, organização de informações e análise de dados de forma mais estruturada.

Como diferencial, o sistema integra uma lógica de cálculo de risco com apoio de um serviço complementar em Python, permitindo classificar automaticamente as áreas em níveis de risco e apresentar os resultados em uma interface visual de apoio.

---

## 🏗️ Arquitetura Mínima

A aplicação segue uma arquitetura simples baseada em separação de responsabilidades, utilizando o padrão de desenvolvimento em camadas.

### 🔹 Backend

O backend é desenvolvido em Java utilizando o framework Spring Boot. Ele é responsável por:

- Gerenciar as regras de negócio do sistema  
- Organizar e estruturar os dados  
- Expor endpoints REST para acesso às informações  
- Integrar o sistema principal com o serviço complementar de cálculo de risco  

A aplicação possui controladores responsáveis por receber requisições HTTP e retornar respostas no formato JSON.

---

### 🔹 Estrutura de Dados

Os dados do sistema são representados por classes Java, DTOs e serviços responsáveis por organizar os fluxos de cadastro, consulta e cálculo de risco.

Atualmente, o sistema trabalha com dados como:

- Identificador da área  
- Nome da área monitorada  
- Unidade de saúde associada  
- Bairro  
- Regional ou distrito  
- População de referência  
- Status da área  
- Indicadores utilizados na análise de risco  

Nesta etapa, o cadastro e a consulta de áreas monitoradas funcionam em memória, sem persistência em banco de dados.

---

### 🔹 API REST

A comunicação com o sistema é feita por meio de endpoints REST. Entre os endpoints implementados estão:

- `POST /api/areas` → cadastra uma nova área monitorada  
- `GET /api/areas` → lista as áreas monitoradas cadastradas  
- `GET /api/areas/{id}` → consulta uma área monitorada pelo identificador  
- `POST /api/areas/calcular-risco` → realiza o cálculo de risco com apoio da integração com Python  

As respostas são fornecidas em formato JSON, permitindo integração com a interface visual e com futuras evoluções do sistema.

---

### 🔹 Front-end

A solução já conta com um protótipo visual desenvolvido em Streamlit, utilizado para exibir informações do sistema e apresentar os resultados do cálculo de risco de forma mais visual e interativa.

Essa camada tem como objetivo permitir:

- Visualização organizada dos dados  
- Apresentação dos resultados do cálculo de risco  
- Apoio à demonstração e validação do fluxo da solução  

---

### 🔹 Serviço complementar em Python

O projeto também conta com um serviço complementar em Python, responsável por executar a lógica específica de cálculo de risco utilizada pela aplicação.

Esse serviço atua de forma integrada ao backend Java, recebendo os dados necessários, processando o cálculo e devolvendo a resposta ao sistema principal.

---

### 🔹 Banco de Dados (Planejado)

Está prevista a integração com um banco de dados relacional, que permitirá:

- Persistência dos dados  
- Armazenamento estruturado das informações  
- Suporte a consultas mais avançadas  
- Evolução do sistema para além do uso em memória  

---

## 🚀 Status do Projeto

Atualmente, o sistema se encontra em desenvolvimento e já apresenta entregas além da Sprint 0, incluindo funcionalidades iniciais da Sprint 1.

No estágio atual, o projeto já possui:

- Estrutura base do backend configurada  
- Endpoints REST funcionando  
- Cadastro de áreas monitoradas em memória  
- Listagem e consulta de áreas monitoradas por identificador  
- Integração entre Java e serviço complementar em Python  
- Protótipo visual em Streamlit  
- Testes unitários iniciais implementados para a camada de serviço  

Essa etapa tem como objetivo validar o fluxo funcional da aplicação, estruturar o sistema para os próximos incrementos e preparar a evolução para persistência, refinamento visual e ampliação das funcionalidades.

---

## 👨‍💻 Integrantes

* Daniela Teixeira Abreu – 4231923259
* Marcela Maria Barbosa - 422222661
* Matheus Felipe Lopes da Silva - 4231925981
* Nátali Isaltino Gomes - 4231925815
* Vinícius Raphael Rios de Lima - 42321398
