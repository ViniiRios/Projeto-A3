import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- 1. CONFIGURAÇÕES GERAIS ---

API_BASE_URL = "http://localhost:8080"

st.set_page_config(
    page_title="VigiA-SUS | Sistema Preditivo",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* 1. Importação de Fonte Personalizada (Montserrat) */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap');
    
    /* 2. Aplicação Global e Cor de Fundo */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 100%) !important;
        background-attachment: fixed;
    }

    [data-testid="stHeader"] {
        background: rgba(0,0,0,0) !important;
    }
    
    /* 3. Customização da Barra Lateral (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #F0F4F8 !important;
        border-right: 2px solid #E2E8F0;
    }
    [data-testid="stSidebar"] * {
        font-size: 16px !important;
    }
    
    /* 4. Títulos e Logo de Login */
    .logo-login { 
        color: #1E3A8A; 
        font-weight: 900; 
        font-size: 85px !important;
        text-align: center; 
        margin-top: -30px; 
        margin-bottom: 0px; 
        letter-spacing: -3px;
        line-height: 1;
    }
    
    .logo-sub { 
        color: #64748B; 
        font-size: 32px !important;
        text-align: center !important;
        width: 100%;
        display: block; 
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 45px; 
        font-weight: 600;
        letter-spacing: -0.5px;
        line-height: 1.2;
    }
    
    /* 5. Destaque para os Labels */
    label {
        font-size: 1.15rem !important;
        color: #1E293B !important;
        font-weight: 700 !important;
        margin-bottom: 8px !important;
    }
    
    /* 6. Caixas de Input */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
        padding: 4px 6px;
        transition: all 0.3s ease;
    }
    
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15) !important;
    }
    
    /* 7. Botões */
    div.stButton > button { 
        background-color: #1E3A8A !important;
        color: white; 
        width: 100%; 
        border-radius: 8px; 
        font-weight: 700; 
        font-size: 20px !important;
        padding: 1rem;
        transition: all 0.3s ease; 
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover { 
        background-color: #1D4ED8; 
        transform: translateY(-2px); 
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    /* 8. Cards de Resultado de Risco */
    .status-box { 
        padding: 35px; 
        border-radius: 16px; 
        text-align: center; 
        margin-top: 20px; 
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.2); 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GERENCIAMENTO DE ESTADO ---

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_role' not in st.session_state:
    st.session_state['user_role'] = ""
if 'areas_cadastradas' not in st.session_state:
    st.session_state['areas_cadastradas'] = []

# --- 3. FUNÇÕES AUXILIARES DE INTEGRAÇÃO ---

def buscar_dados_backend(endpoint, mensagem_erro):
    """Busca dados no backend Java/Spring Boot."""
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=10)

        if response.status_code == 200:
            return response.json()

        st.error(f"{mensagem_erro} Código HTTP: {response.status_code}")
        return None

    except Exception as e:
        st.error(f"{mensagem_erro} Verifique se o backend Java está rodando na porta 8080. Detalhes: {e}")
        return None


def preparar_dataframe_areas(areas):
    """Organiza os dados de áreas para exibição no Streamlit."""
    df = pd.DataFrame(areas)

    colunas_esperadas = [
        "codigoArea",
        "bairro",
        "nome",
        "regionalOuDistrito",
        "unidadeSaude",
        "populacaoReferencia",
        "status"
    ]

    colunas_existentes = [col for col in colunas_esperadas if col in df.columns]
    df = df[colunas_existentes]

    df = df.rename(columns={
        "codigoArea": "Código da Área",
        "bairro": "Bairro",
        "nome": "Identificação",
        "regionalOuDistrito": "Regional/Distrito",
        "unidadeSaude": "Unidade de Saúde",
        "populacaoReferencia": "População de Referência",
        "status": "Status"
    })

    if "População de Referência" in df.columns:
        df["População de Referência"] = df["População de Referência"].apply(
            lambda valor: f"{int(valor):,}".replace(",", ".") if pd.notnull(valor) else valor
        )

    return df


def preparar_dataframe_ovitrampas(ovitrampas):
    """Organiza os dados de ovitrampas para exibição no Streamlit."""
    df = pd.DataFrame(ovitrampas)

    colunas_esperadas = [
        "codigoArea",
        "bairro",
        "totalArmadilhas",
        "totalNegativas",
        "percentualNegativas",
        "totalPositivas",
        "percentualPositivas"
    ]

    colunas_existentes = [col for col in colunas_esperadas if col in df.columns]
    df = df[colunas_existentes]

    df = df.rename(columns={
        "codigoArea": "Código da Área",
        "bairro": "Bairro",
        "totalArmadilhas": "Total de Armadilhas",
        "totalNegativas": "Total Negativas",
        "percentualNegativas": "% Negativas",
        "totalPositivas": "Total Positivas",
        "percentualPositivas": "% Positivas"
    })

    return df


def formatar_percentual(valor):
    """Formata percentuais numéricos para exibição."""
    try:
        return f"{float(valor):.2f}%".replace(".", ",")
    except Exception:
        return str(valor)


def montar_opcoes_areas(areas):
    """Monta opções legíveis para seleção de área."""
    df = pd.DataFrame(areas)

    if df.empty or "codigoArea" not in df.columns:
        return []

    df = df.sort_values("codigoArea")

    opcoes = []
    for _, row in df.iterrows():
        codigo = row.get("codigoArea", "")
        bairro = row.get("bairro", "")
        regional = row.get("regionalOuDistrito", "")
        opcoes.append(f"{codigo} - {bairro} ({regional})")

    return opcoes

# --- 4. MÓDULOS DO SISTEMA ---

def modulo_login():
    """Tela de autenticação do sistema."""
    st.markdown('<h1 class="logo-login">VigiA-SUS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="logo-sub">Plataforma de Inteligência e Monitoramento Epidemiológico</p>', unsafe_allow_html=True)
    
    _, col_login, _ = st.columns([1.5, 1, 1.5])
    
    with col_login:
        with st.container(border=True):
            st.markdown("### 🔐 Autenticação de Acesso")
            st.markdown("Insira suas credenciais:")
            
            with st.form("form_auth"):
                username = st.text_input("Usuário (ou E-mail)")
                password = st.text_input("Senha", type="password")
                submit_login = st.form_submit_button("Acessar Plataforma")
                
                if submit_login:
                    if username == "admin" and password == "1234":
                        st.session_state['logged_in'] = True
                        st.session_state['user_role'] = "Gestor de TI"
                        st.rerun()
                    elif username == "analista" and password == "1234":
                        st.session_state['logged_in'] = True
                        st.session_state['user_role'] = "Analista de Dados"
                        st.rerun()
                    else:
                        st.error("❌ Credenciais inválidas! Verifique os dados inseridos.")
                        
            st.caption("Ambiente de Homologação (MVP) | Contas teste: admin/1234 ou analista/1234")


def modulo_dashboard():
    """Painel principal de predição integrado ao backend Java/API de IA em Python."""
    st.markdown('<p class="title-dashboard">📊 Módulo Preditivo de Risco</p>', unsafe_allow_html=True)
    st.markdown("Simulação de cenários epidemiológicos utilizando modelos de regressão validados no backend.")

    with st.sidebar:
        st.markdown("### ☁️ Parâmetros Locais")
        temp_input = st.number_input("Temperatura Média (°C)", min_value=10.0, max_value=45.0, value=25.0, step=0.1)
        precip_input = st.number_input("Pluviosidade (mm)", min_value=0.0, max_value=500.0, value=150.0, step=1.0)
        
        st.markdown("### 📈 Notificações")
        casos_lag1 = st.number_input("Casos (Mês Atual)", 0, 100000, 500)
        casos_lag2 = st.number_input("Casos (Mês Anterior)", 0, 100000, 300)
        populacao = st.number_input("População da Área", 1, 5000000, 2500000)
        
        btn_predicao = st.button("🚀 Executar Motor de Inferência")

    tab_res, tab_met = st.tabs(["Resultados da Análise", "Metodologia Empregada"])
    
    with tab_res:
        st.subheader("Resumo das Variáveis Inseridas")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Temperatura", f"{temp_input}°C")
        c2.metric("Chuva Acumulada", f"{precip_input} mm")
        c3.metric("Total de Notificações", casos_lag1)
        c4.metric("População", f"{populacao:,}".replace(",", "."))
        st.markdown("---")

        if btn_predicao:
            url_java = f"{API_BASE_URL}/api/areas/calcular-risco"
            payload = {
                "temperatura": temp_input,
                "chuva": precip_input,
                "numeroCasos": casos_lag1,
                "casosLag2": casos_lag2,
                "populacao": populacao,
                "mes": datetime.now().month,
                "ano": datetime.now().year
            }

            with st.spinner("Conectando ao backend Java e processando IA..."):
                try:
                    response = requests.post(url_java, json=payload, timeout=10)

                    if response.status_code == 200:
                        res = response.json()
                        nivel_risco = res.get('risco', 'INDETERMINADO').upper()
                        taxa = res.get('taxaIncidencia', 0.0)

                        cores = {
                            "ALERTA MÁXIMO": "#B91C1C",
                            "RISCO MODERADO": "#D97706",
                            "RISCO BAIXO": "#15803D"
                        }
                        cor_fundo = cores.get(nivel_risco, "#1E3A8A")

                        st.markdown(f"""
                            <div class="status-box" style="background-color: {cor_fundo};">
                                <h2 style="color: white; margin:0; font-size: 32px;">
                                    ESTADO IDENTIFICADO: {nivel_risco}
                                </h2>
                                <p style="color: rgba(255,255,255,0.9); font-size: 18px; margin-top: 10px;">
                                    Taxa de Incidência Calculada: <b>{taxa:.2f}</b> por 100 mil/hab.
                                </p>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.error(f"Erro na requisição. Código HTTP: {response.status_code}")

                except Exception as e:
                    st.error(f"⚠️ Motor Backend Indisponível. Certifique-se de que o Java (porta 8080) está rodando. Detalhes: {e}")
        else:
            st.info("Aguardando execução. Ajuste os parâmetros na barra lateral e clique em 'Executar Motor de Inferência'.")

    with tab_met:
        st.markdown("### Fundamentação Teórica")
        st.write(
            "A classificação de risco utiliza uma arquitetura híbrida, integrando um backend em "
            "**Java 17 (Spring Boot)** para processamento de regras de negócio e cálculo da Taxa de "
            "Incidência (casos x 100.000 / população), com um serviço de inteligência artificial em "
            "**Python (Flask)** responsável por avaliar a probabilidade de eclosão de vetores baseando-se "
            "em variáveis climáticas e séries temporais epidemiológicas."
        )


def modulo_cadastro():
    """Tela de gestão territorial com consulta real de áreas, ovitrampas e cadastro manual MVP."""
    st.markdown('<p class="title-dashboard">📂 Gestão Territorial de Saúde</p>', unsafe_allow_html=True)
    st.markdown(
        "Consulta e acompanhamento das áreas monitoradas pelo sistema, com dados persistidos no "
        "backend Java e no banco PostgreSQL."
    )

    tab_areas, tab_ovitrampas, tab_cadastro = st.tabs([
        "Áreas Monitoradas",
        "Ovitrampas por Área",
        "Cadastro Manual MVP"
    ])

    with tab_areas:
        st.markdown("### 🗺️ Áreas Monitoradas")
        st.caption("Dados carregados do backend Java a partir da tabela `areas` no PostgreSQL.")

        if st.button("🔄 Atualizar dados das áreas"):
            st.rerun()

        areas = buscar_dados_backend(
            "/api/areas",
            "Não foi possível carregar as áreas monitoradas."
        )

        if areas is None:
            st.info("Aguardando conexão com o backend para exibir as áreas monitoradas.")
        elif len(areas) == 0:
            st.warning("Nenhuma área monitorada foi encontrada no banco de dados.")
        else:
            df_areas = preparar_dataframe_areas(areas)

            total_areas = len(df_areas)
            total_ativas = 0
            total_regionais = 0

            if "Status" in df_areas.columns:
                total_ativas = df_areas[df_areas["Status"].str.upper() == "ATIVA"].shape[0]

            if "Regional/Distrito" in df_areas.columns:
                total_regionais = df_areas["Regional/Distrito"].nunique()

            c1, c2, c3 = st.columns(3)
            c1.metric("Áreas cadastradas", total_areas)
            c2.metric("Áreas ativas", total_ativas)
            c3.metric("Regionais/Distritos", total_regionais)

            st.markdown("#### Base territorial cadastrada")
            st.dataframe(df_areas, use_container_width=True)

    with tab_ovitrampas:
        st.markdown("### 🧪 Monitoramento de Ovitrampas por Área")
        st.caption(
            "Consulta dos indicadores entomológicos vinculados às áreas monitoradas. "
            "Os dados são carregados do endpoint `/api/ovitrampas/area/{codigoArea}`."
        )

        areas = buscar_dados_backend(
            "/api/areas",
            "Não foi possível carregar a lista de áreas para consulta de ovitrampas."
        )

        if areas is None or len(areas) == 0:
            st.warning("Não foi possível carregar as áreas para seleção.")
        else:
            opcoes_area = montar_opcoes_areas(areas)

            area_selecionada = st.selectbox(
                "Selecione uma área monitorada",
                opcoes_area
            )

            codigo_area = area_selecionada.split(" - ")[0].strip()

            st.markdown(f"**Área selecionada:** `{area_selecionada}`")

            ovitrampas = buscar_dados_backend(
                f"/api/ovitrampas/area/{codigo_area}",
                "Não foi possível carregar os dados de ovitrampas para a área selecionada."
            )

            if ovitrampas is None:
                st.info("Aguardando retorno do backend para os dados de ovitrampas.")
            elif len(ovitrampas) == 0:
                st.warning("Nenhum registro de ovitrampas foi encontrado para esta área.")
            else:
                df_ovitrampas = preparar_dataframe_ovitrampas(ovitrampas)

                primeiro_registro = ovitrampas[0]

                total_armadilhas = primeiro_registro.get("totalArmadilhas", 0)
                total_positivas = primeiro_registro.get("totalPositivas", 0)
                total_negativas = primeiro_registro.get("totalNegativas", 0)
                percentual_positivas = primeiro_registro.get("percentualPositivas", 0)

                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Total de armadilhas", total_armadilhas)
                c2.metric("Positivas", total_positivas)
                c3.metric("Negativas", total_negativas)
                c4.metric("% Positivas", formatar_percentual(percentual_positivas))

                st.markdown("#### Indicadores entomológicos da área")
                st.dataframe(df_ovitrampas, use_container_width=True)

    with tab_cadastro:
        st.markdown("### 📝 Cadastro Manual de Área")
        st.info(
            "Nesta versão, o cadastro manual permanece como recurso MVP temporário. "
            "A consulta oficial das áreas monitoradas está integrada ao backend e ao banco na aba "
            "**Áreas Monitoradas**."
        )

        with st.form("form_area"):
            st.markdown("**Cadastrar Nova Área de Abrangência**")
            c1, c2 = st.columns(2)
            nome_area = c1.text_input("Identificação da Área (Ex: Regional Pampulha)")
            unidade_ref = c1.text_input("Unidade Básica de Saúde (UBS) Referência")
            bairro = c2.text_input("Bairros Contemplados")
            pop_area = c2.number_input("Estimativa Populacional", min_value=1, step=100)
            
            submit_area = st.form_submit_button("Registrar no Sistema")
            
            if submit_area:
                if nome_area and unidade_ref:
                    nova_area = {
                        "ID Área": f"AR-{len(st.session_state['areas_cadastradas'])+1:03d}",
                        "Identificação": nome_area,
                        "UBS Referência": unidade_ref,
                        "Bairros": bairro,
                        "População": pop_area,
                        "Data de Inclusão": datetime.now().strftime("%d/%m/%Y")
                    }
                    st.session_state['areas_cadastradas'].append(nova_area)
                    st.success(f"Área '{nome_area}' incluída temporariamente na sessão do protótipo.")
                else:
                    st.warning("⚠️ Os campos 'Identificação' e 'UBS Referência' são de preenchimento obrigatório.")

        st.markdown("---")
        st.markdown("**Prévia temporária da sessão atual**")

        if st.session_state['areas_cadastradas']:
            st.dataframe(pd.DataFrame(st.session_state['areas_cadastradas']), use_container_width=True)
        else:
            st.info("Nenhuma área foi cadastrada manualmente nesta sessão.")


def modulo_importacao():
    """Tela de submissão e validação de arquivos estruturados (CSV)."""
    st.markdown('<p class="title-dashboard">📥 Integração e Validação de Insumos</p>', unsafe_allow_html=True)
    st.markdown("Módulo destinado à carga de planilhas de ovitrampas e notificações epidemiológicas padronizadas.")

    c_upload, c_validacao = st.columns([2, 1])
    
    with c_upload:
        arquivo = st.file_uploader("Anexar Lote de Dados (Formato .CSV)", type="csv")
        if arquivo:
            try:
                df = pd.read_csv(arquivo)
                st.write("Pré-visualização do Lote (Amostra 5 registros):")
                st.dataframe(df.head(5), use_container_width=True)
            except Exception:
                st.error("Erro na leitura do arquivo. Certifique-se de que é um CSV válido delimitado por vírgulas.")

    with c_validacao:
        st.markdown("### Protocolo de Validação")
        st.checkbox("Integridade de Cabeçalhos", value=bool(arquivo), disabled=True)
        st.checkbox("Tipagem de Variáveis Contínuas", value=bool(arquivo), disabled=True)
        st.checkbox("Consistência Georreferencial", value=bool(arquivo), disabled=True)
        
        st.write("")
        if st.button("Iniciar Pipeline de Processamento"):
            if arquivo:
                st.success("Dados aprovados nas regras de negócio. Prontos para persistência.")
            else:
                st.error("Nenhum lote de dados anexado.")


def modulo_admin():
    """Painel de administração exclusivo para Gestores de TI."""
    st.markdown('<p class="title-dashboard">👥 Administração de Acessos</p>', unsafe_allow_html=True)
    
    st.markdown("**Corpo Técnico Habilitado (Simulação)**")
    membros = [
        {"Matrícula": "4231923259", "Colaborador": "Daniela Teixeira Abreu", "Perfil": "Gestor de TI", "Status": "Ativo"},
        {"Matrícula": "422222661", "Colaborador": "Marcela Maria Barbosa", "Perfil": "Analista de Dados", "Status": "Ativo"},
        {"Matrícula": "4231925981", "Colaborador": "Matheus Felipe Lopes", "Perfil": "Analista de Dados", "Status": "Ativo"},
        {"Matrícula": "4231925815", "Colaborador": "Nátali Isaltino Gomes", "Perfil": "Operador de Importação", "Status": "Ativo"},
        {"Matrícula": "42321398", "Colaborador": "Vinícius Raphael Rios", "Perfil": "Operador de Importação", "Status": "Ativo"}
    ]
    st.table(pd.DataFrame(membros))

# --- 5. ROTEADOR PRINCIPAL E CONTROLE DE ACESSO (RBAC) ---

if not st.session_state['logged_in']:
    modulo_login()
else:
    role = st.session_state['user_role']
    
    with st.sidebar:
        st.markdown(f"**Credencial Ativa:**")
        st.info(f"👤 {role}")
        st.markdown("---")
        
        opcoes_menu = ["Dashboard Preditivo"]
        
        if role == "Gestor de TI":
            opcoes_menu.extend(["Gestão Territorial", "Administração de Acessos", "Importação de Insumos"])
        elif role == "Analista de Dados":
            opcoes_menu.extend(["Importação de Insumos"])
            
        navegacao = st.radio("Módulos do Sistema", opcoes_menu)
        
        st.markdown("---")
        if st.button("Encerrar Sessão", type="secondary"):
            st.session_state['logged_in'] = False
            st.session_state['areas_cadastradas'] = []
            st.rerun()

    if navegacao == "Dashboard Preditivo":
        modulo_dashboard()
    elif navegacao == "Gestão Territorial":
        modulo_cadastro()
    elif navegacao == "Administração de Acessos":
        modulo_admin()
    elif navegacao == "Importação de Insumos":
        modulo_importacao()

    st.markdown("---")
    st.markdown(
        f"<p style='text-align: center; color: #94A3B8; font-size: 12px;'>"
        f"Projeto Acadêmico - Ciência da Computação | VigiA-SUS MVP v1.0 | {datetime.now().year}"
        f"</p>",
        unsafe_allow_html=True
    )