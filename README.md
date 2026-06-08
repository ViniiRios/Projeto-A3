# Sistema de Monitoramento Epidemiológico — VigiA-SUS

## 📌 Resumo do Projeto

O **VigiA-SUS** é um sistema acadêmico de monitoramento epidemiológico desenvolvido para apoiar a análise de risco em saúde pública. A aplicação organiza dados territoriais, epidemiológicos, climáticos e entomológicos, permitindo consultar áreas monitoradas, acompanhar indicadores de ovitrampas, validar insumos e executar uma análise preditiva de risco. O sistema possui backend em Java/Spring Boot, banco PostgreSQL, serviço complementar em Python para apoio ao cálculo preditivo e interface visual em Streamlit. O objetivo é oferecer uma ferramenta de apoio à tomada de decisão para equipes de vigilância e gestão em saúde.

## 🎯 Problema que resolve e público-alvo

O monitoramento epidemiológico envolve dados de diferentes origens, como notificações de doenças, clima, território, população e indicadores de vetores. Quando essas informações ficam dispersas, a análise de risco se torna mais lenta e menos padronizada.

O VigiA-SUS busca centralizar essas informações em uma plataforma única, facilitando a consulta, a análise e a classificação de risco epidemiológico.

**Público-alvo:**

* gestores epidemiológicos;
* analistas de vigilância;
* analistas de dados;
* operadores de importação de insumos;
* profissionais e equipes de saúde pública.

## ✨ Funcionalidades

* Autenticação de usuários com login e senha.
* Controle de acesso por perfil de usuário.
* Dashboard Preditivo para análise de risco epidemiológico.
* Cálculo da taxa atual de incidência.
* Integração com serviço Python para estimativa preditiva de risco.
* Exibição do índice preditivo considerado, taxa atual, taxa prevista e casos estimados.
* Consulta de dados regionais de casos e clima.
* Listagem de áreas monitoradas.
* Cadastro de novas áreas monitoradas.
* Geração automática do código da área.
* Inativação e reativação de áreas sem exclusão do banco.
* Consulta de indicadores de ovitrampas por área.
* Pré-validação de arquivos CSV de insumos.
* Download de modelos CSV.
* Histórico temporário de validações de insumos.
* Tela informativa sobre o projeto e a equipe.

## 🛠️ Tecnologias utilizadas

### Backend

* Java
* Spring Boot
* Maven
* Spring Data JPA
* PostgreSQL
* API REST

### Frontend

* Python
* Streamlit
* Pandas
* Requests

### Serviço preditivo

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* XGBoost

### Testes

* JUnit 5
* Mockito
* Cucumber
* Gherkin
* Maven

### Ferramentas de apoio

* Visual Studio Code
* Postman
* DBeaver
* GitHub
* GitHub Issues/Projects

## ▶️ Como executar o projeto

A aplicação completa roda localmente com três partes abertas separadamente:

1. backend Java/Spring Boot;
2. serviço Python de IA;
3. frontend Streamlit.

### 1. Executar o backend Java

No terminal, acesse a pasta:

```bash
cd systemvigiasus
```

Execute:

```bash
.\mvnw.cmd spring-boot:run
```

O backend será iniciado em:

```text
http://localhost:8080
```

### 2. Executar o serviço Python

Em outro terminal, acesse a pasta:

```bash
cd ai-engine
```

Execute:

```bash
py main.py
```

O serviço Python será iniciado em:

```text
http://localhost:5000
```

### 3. Executar o frontend Streamlit

Em outro terminal, acesse a pasta:

```bash
cd frontend-prototype
```

Execute:

```bash
py -m streamlit run app_streamlit.py
```

O sistema será aberto no navegador em:

```text
http://localhost:8501
```

## 👤 Usuários de teste

| Usuário    | Senha  | Nome                   | Perfil                 |
| ---------- | ------ | ---------------------- | ---------------------- |
| `daniela`  | `1234` | Daniela Teixeira Abreu | Gestor de TI           |
| `vinicius` | `1234` | Vinícius Raphael Rios  | Gestor Epidemiológico  |
| `matheus`  | `1234` | Matheus Felipe Lopes   | Analista de Dados      |
| `natali`   | `1234` | Nátali Isaltino Gomes  | Operador de Importação |
| `marcela`  | `1234` | Marcela Maria Barbosa  | Analista de Vigilância |

## 🧱 Estrutura de pastas

```text
Projeto-A3/
├── ai-engine/
│   ├── dados/
│   ├── model/
│   ├── scripts/
│   ├── main.py
│   └── requirements.txt
│
├── frontend-prototype/
│   └── app_streamlit.py
│
├── systemvigiasus/
│   ├── src/
│   │   ├── main/
│   │   └── test/
│   └── pom.xml
│
├── docs/
│   ├── requisitos/
│   └── testes/
│
├── slides/
└── README.md
```

## 🧪 Como rodar os testes

Na pasta do backend:

```bash
cd systemvigiasus
```

Execute:

```bash
.\mvnw.cmd clean test
```

Esse comando executa:

* testes unitários com JUnit e Mockito;
* cenários BDD automatizados com Cucumber;
* validação do build do backend.

Resultado esperado:

```text
BUILD SUCCESS
```

Os cenários BDD ficam em:

```text
systemvigiasus/src/test/resources/features/
```

O relatório HTML do Cucumber é gerado em:

```text
systemvigiasus/target/cucumber-report.html
```

## 👥 Integrantes e papéis na Sprint

| Integrante                    | Matrícula  | Papel/Atuação                                                                                                   |
| ----------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------- |
| Daniela Teixeira Abreu        | 4231923259 | Implementação inicial da IA, organização da documentação, estrutura de pastas e ajustes visuais/frontend        |
| Marcela Maria Barbosa         | 422222661  | Apoio na validação funcional e testes do sistema                                                                |
| Matheus Felipe Lopes da Silva | 4231925981 | Tratamento de planilhas, organização de dados e apoio à base epidemiológica/climática                           |
| Nátali Isaltino Gomes         | 4231925815 | Apoio no frontend, validação de telas e importação de insumos                                                   |
| Vinícius Raphael Rios de Lima | 42321398   | Backend, banco de dados, integração Java/Python, refinamento da IA, testes automatizados e documentação técnica |
