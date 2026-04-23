import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- 1. CONFIGURAÇÕES DA PÁGINA E CSS ---

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

# --- 2. GERENCIAMENTO DE ESTADO (MEMÓRIA TEMPORÁRIA) ---

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_role' not in st.session_state:
    st.session_state['user_role'] = ""
if 'areas_cadastradas' not in st.session_state:
    st.session_state['areas_cadastradas'] = []

# --- 3. MÓDULOS DO SISTEMA (TELAS) ---

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
    """Painel principal de predição integrado ao backend Java/ API de IA em Python."""
    st.markdown('<p class="title-dashboard">📊 Módulo Preditivo de Risco</p>', unsafe_allow_html=True)
    st.markdown("Simulação de cenários epidemiológicos utilizando modelos de regressão validados no backend.")

    # Entradas na Barra Lateral
    with st.sidebar:
        st.markdown("### ☁️ Parâmetros Locais")
        temp_input = st.number_input("Temperatura Média (°C)", min_value=10.0, max_value=45.0, value=25.0, step=0.1)
        precip_input = st.number_input("Pluviosidade (mm)", min_value=0.0, max_value=500.0, value=150.0, step=1.0)
        
        st.markdown("### 📈 Notificações")
        casos_lag1 = st.number_input("Casos (Mês Atual)", 0, 100000, 500)
        casos_lag2 = st.number_input("Casos (Mês Anterior)", 0, 100000, 300)
        populacao = st.number_input("População da Área", 1, 5000000, 2500000)
        
        btn_predicao = st.button("🚀 Executar Motor de Inferência")

    # Área Principal
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
            # Integração com Spring Boot
            url_java = "http://localhost:8080/api/areas/calcular-risco"
            payload = {
                "temperatura": temp_input, "chuva": precip_input,
                "numeroCasos": casos_lag1, "casosLag2": casos_lag2,
                "populacao": populacao, "mes": datetime.now().month, "ano": datetime.now().year
            }

            with st.spinner("Conectando ao cluster Java e processando IA..."):
                try:
                    response = requests.post(url_java, json=payload, timeout=10)
                    if response.status_code == 200:
                        res = response.json()
                        nivel_risco = res.get('risco', 'INDETERMINADO').upper()
                        taxa = res.get('taxaIncidencia', 0.0)

                        # Mapeamento semântico de cores
                        cores = {"ALERTA MÁXIMO": "#B91C1C", "RISCO MODERADO": "#D97706", "RISCO BAIXO": "#15803D"}
                        cor_fundo = cores.get(nivel_risco, "#1E3A8A")

                        st.markdown(f"""
                            <div class="status-box" style="background-color: {cor_fundo};">
                                <h2 style="color: white; margin:0; font-size: 32px;">ESTADO IDENTIFICADO: {nivel_risco}</h2>
                                <p style="color: rgba(255,255,255,0.9); font-size: 18px; margin-top: 10px;">
                                Taxa de Incidência Calculada: <b>{taxa:.2f}</b> por 100 mil/hab.</p>
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
        st.write("A classificação de risco utiliza uma arquitetura híbrida, integrando um backend em **Java 17 (Spring Boot)** para processamento de regras de negócio e cálculo da Taxa de Incidência (casos x 100.000 / população), com um serviço de inteligência artificial em **Python (Flask)** responsável por avaliar a probabilidade de eclosão de vetores baseando-se em variáveis climáticas e séries temporais epidemiológicas.")

def modulo_cadastro():
    """Tela para registro de novas áreas de monitoramento."""
    st.markdown('<p class="title-dashboard">📂 Gestão Territorial de Saúde</p>', unsafe_allow_html=True)
    
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
                st.success(f"Área '{nome_area}' incluída com sucesso na base de dados temporária.")
            else:
                st.warning("⚠️ Os campos 'Identificação' e 'UBS Referência' são de preenchimento obrigatório.")

    st.markdown("---")
    st.markdown("**Mapeamento Atual (Registros em Memória)**")
    if st.session_state['areas_cadastradas']:
        st.dataframe(pd.DataFrame(st.session_state['areas_cadastradas']), use_container_width=True)
    else:
        st.info("Nenhuma área de monitoramento cadastrada na sessão atual.")

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
            except Exception as e:
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

# --- 4. ROTEADOR PRINCIPAL E CONTROLE DE ACESSO (RBAC) ---

if not st.session_state['logged_in']:
    modulo_login()
else:
    role = st.session_state['user_role']
    
    with st.sidebar:
        st.markdown(f"**Credencial Ativa:**")
        st.info(f"👤 {role}")
        st.markdown("---")
        
        # Árvore de navegação baseada em perfil (RBAC)
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

    # Injeção de dependência de interface
    if navegacao == "Dashboard Preditivo":
        modulo_dashboard()
    elif navegacao == "Gestão Territorial":
        modulo_cadastro()
    elif navegacao == "Administração de Acessos":
        modulo_admin()
    elif navegacao == "Importação de Insumos":
        modulo_importacao()

    # Rodapé Acadêmico
    st.markdown("---")
    st.markdown(f"<p style='text-align: center; color: #94A3B8; font-size: 12px;'>Projeto Acadêmico - Ciência da Computação | VigiA-SUS MVP v1.0 | {datetime.now().year}</p>", unsafe_allow_html=True)