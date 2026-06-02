import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- 1. CONFIGURAÇÕES GERAIS ---

API_BASE_URL = "http://localhost:8080"

REGIONAIS = [
    "BARREIRO",
    "CENTRO-SUL",
    "LESTE",
    "NORDESTE",
    "NOROESTE",
    "NORTE",
    "OESTE",
    "PAMPULHA",
    "VENDA NOVA"
]

PERFIS_COM_GESTAO_COMPLETA = [
    "Gestor de TI",
    "Gestor Epidemiológico"
]

PERFIS_COM_GESTAO_CONSULTA = [
    "Gestor de TI",
    "Gestor Epidemiológico",
    "Analista de Dados",
    "Analista de Vigilância"
]

PERFIS_COM_IMPORTACAO = [
    "Gestor de TI",
    "Gestor Epidemiológico",
    "Analista de Dados",
    "Operador de Importação"
]

CONFIG_INSUMOS = {
    "Áreas monitoradas": {
        "arquivo_modelo": "modelo_areas.csv",
        "descricao": "Base territorial de áreas monitoradas pelo sistema.",
        "colunas": [
            "codigo_area",
            "nome",
            "unidade_saude",
            "bairro",
            "regional_ou_distrito",
            "populacao_referencia",
            "status"
        ],
        "exemplo": {
            "codigo_area": "000",
            "nome": "BHZ NORT",
            "unidade_saude": "CENTRO DE SAUDE AARAO REIS",
            "bairro": "AARAO REIS",
            "regional_ou_distrito": "NORTE",
            "populacao_referencia": "213427",
            "status": "ATIVA"
        }
    },
    "Ovitrampas": {
        "arquivo_modelo": "modelo_ovitrampas.csv",
        "descricao": "Indicadores entomológicos consolidados por área monitorada.",
        "colunas": [
            "codigo_area",
            "bairro",
            "total_armadilhas",
            "total_negativas",
            "percentual_negativas",
            "total_positivas",
            "percentual_positivas"
        ],
        "exemplo": {
            "codigo_area": "000",
            "bairro": "AARAO REIS",
            "total_armadilhas": "100",
            "total_negativas": "62",
            "percentual_negativas": "62",
            "total_positivas": "38",
            "percentual_positivas": "38"
        }
    },
    "Casos e clima": {
        "arquivo_modelo": "modelo_casos_clima.csv",
        "descricao": "Base epidemiológica e climática consolidada por regional.",
        "colunas": [
            "periodo_referencia",
            "regional",
            "casos_dengue",
            "casos_chikungunya",
            "casos_zika",
            "casos_total",
            "temperatura_media",
            "precipitacao_total",
            "populacao_regional"
        ],
        "exemplo": {
            "periodo_referencia": "2017-01 até 2017-12",
            "regional": "Barreiro",
            "casos_dengue": "659",
            "casos_chikungunya": "26",
            "casos_zika": "14",
            "casos_total": "699",
            "temperatura_media": "20,5 °C",
            "precipitacao_total": "1215,4 mm",
            "populacao_regional": "278.144"
        }
    }
}

st.set_page_config(
    page_title="VigiA-SUS | Sistema Preditivo",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap');
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 100%) !important;
        background-attachment: fixed;
    }

    [data-testid="stHeader"] {
        background: rgba(0,0,0,0) !important;
    }
    
    [data-testid="stSidebar"] {
        background-color: #F0F4F8 !important;
        border-right: 2px solid #E2E8F0;
    }

    [data-testid="stSidebar"] * {
        font-size: 16px !important;
    }
    
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
    
    label {
        font-size: 1.15rem !important;
        color: #1E293B !important;
        font-weight: 700 !important;
        margin-bottom: 8px !important;
    }
    
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
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ""
if 'historico_importacoes' not in st.session_state:
    st.session_state['historico_importacoes'] = []

# --- 3. FUNÇÕES AUXILIARES DE INTEGRAÇÃO ---

def autenticar_usuario_backend(username, senha):
    try:
        payload = {
            "username": username,
            "senha": senha
        }

        response = requests.post(f"{API_BASE_URL}/api/auth/login", json=payload, timeout=10)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            return None

        st.error(f"Erro ao autenticar usuário. Código HTTP: {response.status_code}")
        return None

    except Exception as e:
        st.error(f"Não foi possível conectar ao backend de autenticação. Verifique se o Java está rodando na porta 8080. Detalhes: {e}")
        return None


def buscar_dados_backend(endpoint, mensagem_erro):
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=10)

        if response.status_code == 200:
            return response.json()

        st.error(f"{mensagem_erro} Código HTTP: {response.status_code}")
        return None

    except Exception as e:
        st.error(f"{mensagem_erro} Verifique se o backend Java está rodando na porta 8080. Detalhes: {e}")
        return None


def enviar_dados_backend(endpoint, payload, mensagem_erro):
    try:
        response = requests.post(f"{API_BASE_URL}{endpoint}", json=payload, timeout=10)

        if response.status_code in [200, 201]:
            return response.json()

        st.error(f"{mensagem_erro} Código HTTP: {response.status_code}. Resposta: {response.text}")
        return None

    except Exception as e:
        st.error(f"{mensagem_erro} Verifique se o backend Java está rodando na porta 8080. Detalhes: {e}")
        return None


def alterar_status_area(id_area, acao):
    try:
        response = requests.put(f"{API_BASE_URL}/api/areas/{id_area}/{acao}", timeout=10)

        if response.status_code == 200:
            return response.json()

        st.error(f"Não foi possível alterar o status da área. Código HTTP: {response.status_code}")
        return None

    except Exception as e:
        st.error(f"Erro ao alterar status da área. Verifique se o backend está rodando. Detalhes: {e}")
        return None


def preparar_dataframe_areas(areas):
    df = pd.DataFrame(areas)

    colunas_esperadas = [
        "id",
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
        "id": "ID",
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


def preparar_dataframe_casos_clima(casos_clima):
    df = pd.DataFrame(casos_clima)

    colunas_esperadas = [
        "periodoReferencia",
        "regional",
        "casosDengue",
        "casosChikungunya",
        "casosZika",
        "casosTotal",
        "temperaturaMedia",
        "precipitacaoTotal",
        "populacaoRegional"
    ]

    colunas_existentes = [col for col in colunas_esperadas if col in df.columns]
    df = df[colunas_existentes]

    df = df.rename(columns={
        "periodoReferencia": "Período de Referência",
        "regional": "Regional",
        "casosDengue": "Casos de Dengue",
        "casosChikungunya": "Casos de Chikungunya",
        "casosZika": "Casos de Zika",
        "casosTotal": "Casos Totais",
        "temperaturaMedia": "Temperatura Média",
        "precipitacaoTotal": "Precipitação Total",
        "populacaoRegional": "População Regional"
    })

    return df


def formatar_percentual(valor):
    try:
        return f"{float(valor):.2f}%".replace(".", ",")
    except Exception:
        return str(valor)


def formatar_numero(valor):
    try:
        return f"{int(valor):,}".replace(",", ".")
    except Exception:
        return str(valor)


def montar_opcoes_areas(areas):
    df = pd.DataFrame(areas)

    if df.empty or "codigoArea" not in df.columns:
        return []

    df = df.sort_values("codigoArea")

    opcoes = []
    for _, row in df.iterrows():
        id_area = row.get("id", "")
        codigo = row.get("codigoArea", "")
        bairro = row.get("bairro", "")
        regional = row.get("regionalOuDistrito", "")
        status = row.get("status", "")
        opcoes.append(f"{id_area} | {codigo} - {bairro} ({regional}) [{status}]")

    return opcoes


def extrair_id_area(opcao_area):
    try:
        return int(opcao_area.split("|")[0].strip())
    except Exception:
        return None


def extrair_codigo_area(opcao_area):
    try:
        parte_codigo = opcao_area.split("|")[1].split("-")[0].strip()
        return parte_codigo
    except Exception:
        return ""


def extrair_status_area(opcao_area):
    try:
        return opcao_area.split("[")[-1].replace("]", "").strip()
    except Exception:
        return ""


# --- 3.1 FUNÇÕES AUXILIARES DE IMPORTAÇÃO ---

def normalizar_coluna(coluna):
    return str(coluna).strip().lower()


def ler_csv_flexivel(arquivo):
    try:
        arquivo.seek(0)
        return pd.read_csv(arquivo, sep=None, engine="python", dtype=str)
    except Exception:
        arquivo.seek(0)
        return pd.read_csv(arquivo, dtype=str)


def gerar_modelo_csv(tipo_insumo):
    configuracao = CONFIG_INSUMOS[tipo_insumo]
    df_modelo = pd.DataFrame([configuracao["exemplo"]])
    return df_modelo.to_csv(index=False).encode("utf-8")


def validar_arquivo_insumo(df, tipo_insumo):
    colunas_esperadas = CONFIG_INSUMOS[tipo_insumo]["colunas"]
    colunas_encontradas = [normalizar_coluna(coluna) for coluna in df.columns]

    colunas_faltantes = [
        coluna for coluna in colunas_esperadas
        if coluna not in colunas_encontradas
    ]

    colunas_extras = [
        coluna for coluna in colunas_encontradas
        if coluna not in colunas_esperadas
    ]

    total_linhas = len(df)
    total_colunas = len(df.columns)

    campos_vazios_por_coluna = {}
    total_campos_vazios = 0

    df_normalizado = df.copy()
    df_normalizado.columns = colunas_encontradas

    for coluna in colunas_esperadas:
        if coluna in df_normalizado.columns:
            vazios = df_normalizado[coluna].isna().sum()
            vazios += (df_normalizado[coluna].astype(str).str.strip() == "").sum()
            campos_vazios_por_coluna[coluna] = int(vazios)
            total_campos_vazios += int(vazios)

    aprovado = len(colunas_faltantes) == 0 and total_linhas > 0

    if aprovado and total_campos_vazios == 0:
        status = "APROVADO"
        mensagem = "Arquivo aprovado na validação estrutural."
    elif aprovado and total_campos_vazios > 0:
        status = "APROVADO COM ALERTAS"
        mensagem = "Arquivo possui as colunas esperadas, mas contém campos vazios."
    else:
        status = "REPROVADO"
        mensagem = "Arquivo não possui todas as colunas obrigatórias ou está vazio."

    return {
        "tipo_insumo": tipo_insumo,
        "status": status,
        "mensagem": mensagem,
        "total_linhas": total_linhas,
        "total_colunas": total_colunas,
        "colunas_esperadas": colunas_esperadas,
        "colunas_encontradas": colunas_encontradas,
        "colunas_faltantes": colunas_faltantes,
        "colunas_extras": colunas_extras,
        "campos_vazios_por_coluna": campos_vazios_por_coluna,
        "total_campos_vazios": total_campos_vazios
    }


def registrar_historico_importacao(nome_arquivo, resultado_validacao, usuario):
    registro = {
        "Data/Hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Arquivo": nome_arquivo,
        "Tipo de Insumo": resultado_validacao["tipo_insumo"],
        "Usuário": usuario,
        "Status": resultado_validacao["status"],
        "Linhas": resultado_validacao["total_linhas"],
        "Colunas": resultado_validacao["total_colunas"],
        "Campos Vazios": resultado_validacao["total_campos_vazios"]
    }

    st.session_state["historico_importacoes"].append(registro)


def exibir_resultado_validacao(resultado):
    status = resultado["status"]

    if status == "APROVADO":
        st.success(resultado["mensagem"])
    elif status == "APROVADO COM ALERTAS":
        st.warning(resultado["mensagem"])
    else:
        st.error(resultado["mensagem"])

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Linhas analisadas", resultado["total_linhas"])
    c2.metric("Colunas encontradas", resultado["total_colunas"])
    c3.metric("Colunas faltantes", len(resultado["colunas_faltantes"]))
    c4.metric("Campos vazios", resultado["total_campos_vazios"])

    st.markdown("#### Resultado da conferência estrutural")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("**Colunas esperadas**")
        st.dataframe(
            pd.DataFrame({"Coluna esperada": resultado["colunas_esperadas"]}),
            use_container_width=True,
            hide_index=True
        )

    with col_b:
        st.markdown("**Colunas encontradas no arquivo**")
        st.dataframe(
            pd.DataFrame({"Coluna encontrada": resultado["colunas_encontradas"]}),
            use_container_width=True,
            hide_index=True
        )

    if resultado["colunas_faltantes"]:
        st.markdown("#### Colunas faltantes")
        st.error(", ".join(resultado["colunas_faltantes"]))

    if resultado["colunas_extras"]:
        st.markdown("#### Colunas extras")
        st.info(", ".join(resultado["colunas_extras"]))

    if resultado["total_campos_vazios"] > 0:
        st.markdown("#### Campos vazios por coluna")
        df_vazios = pd.DataFrame(
            list(resultado["campos_vazios_por_coluna"].items()),
            columns=["Coluna", "Campos vazios"]
        )
        st.dataframe(df_vazios, use_container_width=True, hide_index=True)

# --- 4. MÓDULOS DO SISTEMA ---

def modulo_login():
    st.markdown('<h1 class="logo-login">VigiA-SUS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="logo-sub">Plataforma de Inteligência e Monitoramento Epidemiológico</p>', unsafe_allow_html=True)
    
    _, col_login, _ = st.columns([1.5, 1, 1.5])
    
    with col_login:
        with st.container(border=True):
            st.markdown("### 🔐 Autenticação de Acesso")
            st.markdown("Insira suas credenciais:")
            
            with st.form("form_auth"):
                username = st.text_input("Usuário")
                password = st.text_input("Senha", type="password")
                submit_login = st.form_submit_button("Acessar Plataforma")
                
                if submit_login:
                    if not username or not password:
                        st.warning("Informe usuário e senha para acessar o sistema.")
                    else:
                        usuario = autenticar_usuario_backend(username, password)

                        if usuario is not None:
                            st.session_state['logged_in'] = True
                            st.session_state['user_role'] = usuario.get("perfil", "")
                            st.session_state['user_name'] = usuario.get("nome", username)
                            st.rerun()
                        else:
                            st.error("❌ Credenciais inválidas ou usuário inativo.")

            st.caption("Login validado pelo backend e pela tabela de usuários no PostgreSQL.")


def modulo_dashboard():
    st.markdown('<p class="title-dashboard">📊 Módulo Preditivo de Risco</p>', unsafe_allow_html=True)
    st.markdown("Simulação de cenários epidemiológicos utilizando modelos de regressão validados no backend.")

    st.markdown("### ⚙️ Parâmetros da Análise")

    with st.container(border=True):
        st.caption("Informe os dados epidemiológicos e climáticos para executar a simulação de risco.")

        c1, c2, c3 = st.columns(3)
        temp_input = c1.number_input("Temperatura Média (°C)", min_value=10.0, max_value=45.0, value=25.0, step=0.1)
        precip_input = c2.number_input("Pluviosidade (mm)", min_value=0.0, max_value=500.0, value=150.0, step=1.0)
        populacao = c3.number_input("População da Área", 1, 5000000, 2500000)

        c4, c5, c6 = st.columns(3)
        casos_lag1 = c4.number_input("Casos (Mês Atual)", 0, 100000, 500)
        casos_lag2 = c5.number_input("Casos (Mês Anterior)", 0, 100000, 300)

        with c6:
            st.markdown("<br>", unsafe_allow_html=True)
            btn_predicao = st.button("🚀 Executar Motor de Inferência")

    tab_res, tab_dados_regionais, tab_met = st.tabs([
        "Resultados da Análise",
        "Dados Regionais",
        "Metodologia Empregada"
    ])
    
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
            st.info("Aguardando execução. Ajuste os parâmetros acima e clique em 'Executar Motor de Inferência'.")

    with tab_dados_regionais:
        st.markdown("### 🌎 Dados Epidemiológicos e Climáticos Regionais")
        st.caption(
            "Consulta dos registros importados na tabela `casos_clima`, contendo casos por agravo, "
            "população regional, temperatura média e precipitação total do período analisado."
        )

        casos_clima = buscar_dados_backend(
            "/api/casos-clima",
            "Não foi possível carregar os dados epidemiológicos e climáticos."
        )

        if casos_clima is None:
            st.info("Aguardando conexão com o backend para exibir os dados regionais.")
        elif len(casos_clima) == 0:
            st.warning("Nenhum registro de casos e clima foi encontrado no banco de dados.")
        else:
            df_casos_clima = preparar_dataframe_casos_clima(casos_clima)

            total_regionais = len(df_casos_clima)
            maior_total_casos = 0
            regional_maior_casos = "Não identificado"
            periodo_referencia = "Não informado"

            if "Casos Totais" in df_casos_clima.columns:
                df_casos_clima["Casos Totais"] = pd.to_numeric(df_casos_clima["Casos Totais"], errors="coerce")
                maior_total_casos = int(df_casos_clima["Casos Totais"].max())

                linha_maior_casos = df_casos_clima.loc[df_casos_clima["Casos Totais"].idxmax()]
                regional_maior_casos = linha_maior_casos.get("Regional", "Não identificado")

            if "Período de Referência" in df_casos_clima.columns:
                periodo_referencia = df_casos_clima["Período de Referência"].iloc[0]

            c1, c2, c3 = st.columns(3)
            c1.metric("Regionais analisadas", total_regionais)
            c2.metric("Maior total de casos", formatar_numero(maior_total_casos))
            c3.metric("Regional com maior registro", regional_maior_casos)

            st.markdown(f"**Período de referência:** `{periodo_referencia}`")
            st.info(
                "Observação: nesta versão, temperatura média e precipitação total representam o cenário "
                "climático médio do período analisado. Os casos e a população variam por regional."
            )

            st.markdown("#### Base epidemiológica e climática por regional")
            st.dataframe(df_casos_clima, use_container_width=True)

    with tab_met:
        st.markdown("### Fundamentação Teórica")
        st.write(
            "A classificação de risco utiliza uma arquitetura híbrida, integrando um backend em "
            "**Java 17 (Spring Boot)** para processamento de regras de negócio e cálculo da Taxa de "
            "Incidência (casos x 100.000 / população), com um serviço de inteligência artificial em "
            "**Python (Flask)** responsável por avaliar a probabilidade de eclosão de vetores baseando-se "
            "em variáveis climáticas e séries temporais epidemiológicas."
        )


def exibir_aba_areas_monitoradas():
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


def exibir_aba_ovitrampas():
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
            opcoes_area,
            key="select_ovitrampas_area"
        )

        codigo_area = extrair_codigo_area(area_selecionada)

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


def exibir_aba_cadastro_area():
    st.markdown("### 📝 Cadastro de Nova Área Monitorada")
    st.info(
        "O código da área será gerado automaticamente pelo backend, seguindo a sequência já existente. "
        "Novas áreas são cadastradas inicialmente com status **ATIVA**."
    )

    with st.form("form_area_real"):
        c1, c2 = st.columns(2)

        nome_area = c1.text_input("Identificação da Área")
        unidade_ref = c1.text_input("Unidade Básica de Saúde (UBS) Referência")
        bairro = c2.text_input("Bairro ou área contemplada")
        regional = c2.selectbox("Regional ou distrito", REGIONAIS)
        pop_area = st.number_input("População de referência estimada", min_value=1, step=100)

        submit_area = st.form_submit_button("Cadastrar Área no Banco")
        
        if submit_area:
            if nome_area and unidade_ref and bairro and regional and pop_area:
                payload = {
                    "nome": nome_area,
                    "unidadeSaude": unidade_ref,
                    "bairro": bairro,
                    "regionalOuDistrito": regional,
                    "populacaoReferencia": pop_area
                }

                response = enviar_dados_backend(
                    "/api/areas",
                    payload,
                    "Não foi possível cadastrar a área."
                )

                if response is not None:
                    st.success(
                        f"Área cadastrada com sucesso. Código gerado: {response.get('codigoArea')} | "
                        f"Status: {response.get('status')}"
                    )
                    st.info("Acesse a aba **Áreas Monitoradas** e clique em **Atualizar dados das áreas** para visualizar o novo registro.")
            else:
                st.warning("Preencha todos os campos obrigatórios antes de cadastrar a área.")


def exibir_aba_manutencao_area():
    st.markdown("### ⚙️ Manutenção de Área Monitorada")
    st.caption(
        "Use esta seção para inativar ou reativar áreas. A área não é excluída do banco; "
        "apenas deixa de participar do monitoramento ativo quando marcada como INATIVA."
    )

    areas = buscar_dados_backend(
        "/api/areas",
        "Não foi possível carregar a lista de áreas para manutenção."
    )

    if areas is None or len(areas) == 0:
        st.warning("Não foi possível carregar as áreas para manutenção.")
    else:
        opcoes_area = montar_opcoes_areas(areas)

        area_selecionada = st.selectbox(
            "Selecione uma área para manutenção",
            opcoes_area,
            key="select_manutencao_area"
        )

        id_area = extrair_id_area(area_selecionada)
        status_area = extrair_status_area(area_selecionada)

        st.markdown(f"**Área selecionada:** `{area_selecionada}`")
        st.markdown(f"**Status atual:** `{status_area}`")

        c1, c2 = st.columns(2)

        with c1:
            if st.button("Inativar área selecionada"):
                response = alterar_status_area(id_area, "inativar")

                if response is not None:
                    st.success(f"Área {response.get('codigoArea')} inativada com sucesso.")
                    st.info("Atualize a página ou retorne à aba para visualizar o novo status.")

        with c2:
            if st.button("Reativar área selecionada"):
                response = alterar_status_area(id_area, "reativar")

                if response is not None:
                    st.success(f"Área {response.get('codigoArea')} reativada com sucesso.")
                    st.info("Atualize a página ou retorne à aba para visualizar o novo status.")


def modulo_cadastro(role):
    st.markdown('<p class="title-dashboard">📂 Gestão Territorial de Saúde</p>', unsafe_allow_html=True)
    st.markdown(
        "Consulta, cadastro e manutenção das áreas monitoradas pelo sistema, com dados persistidos no "
        "backend Java e no banco PostgreSQL."
    )

    if role in PERFIS_COM_GESTAO_COMPLETA:
        tab_areas, tab_ovitrampas, tab_cadastro, tab_manutencao = st.tabs([
            "Áreas Monitoradas",
            "Ovitrampas por Área",
            "Cadastro de Área",
            "Manutenção de Área"
        ])

        with tab_areas:
            exibir_aba_areas_monitoradas()

        with tab_ovitrampas:
            exibir_aba_ovitrampas()

        with tab_cadastro:
            exibir_aba_cadastro_area()

        with tab_manutencao:
            exibir_aba_manutencao_area()

    else:
        tab_areas, tab_ovitrampas = st.tabs([
            "Áreas Monitoradas",
            "Ovitrampas por Área"
        ])

        with tab_areas:
            exibir_aba_areas_monitoradas()

        with tab_ovitrampas:
            exibir_aba_ovitrampas()


def modulo_importacao():
    st.markdown('<p class="title-dashboard">📥 Integração e Validação de Insumos</p>', unsafe_allow_html=True)
    st.markdown(
        "Módulo destinado à conferência de planilhas utilizadas no monitoramento epidemiológico, "
        "com validação de estrutura antes da carga oficial no banco de dados."
    )

    tab_validar, tab_historico, tab_regras = st.tabs([
        "Validar Arquivo",
        "Histórico de Importações",
        "Regras dos Insumos"
    ])

    with tab_validar:
        st.markdown("### 📄 Validação de Arquivo CSV")
        st.info(
            "Nesta versão, a tela realiza a pré-validação dos arquivos antes da persistência oficial. "
            "A carga final dos dados continua sendo controlada no banco PostgreSQL."
        )

        tipo_insumo = st.selectbox(
            "Tipo de insumo",
            list(CONFIG_INSUMOS.keys())
        )

        configuracao = CONFIG_INSUMOS[tipo_insumo]

        st.caption(configuracao["descricao"])

        modelo_csv = gerar_modelo_csv(tipo_insumo)

        st.download_button(
            label="⬇️ Baixar modelo CSV",
            data=modelo_csv,
            file_name=configuracao["arquivo_modelo"],
            mime="text/csv"
        )

        arquivo = st.file_uploader(
            "Anexar arquivo CSV para validação",
            type="csv",
            key="upload_insumo_csv"
        )

        if arquivo:
            try:
                df = ler_csv_flexivel(arquivo)
                resultado = validar_arquivo_insumo(df, tipo_insumo)

                exibir_resultado_validacao(resultado)

                st.markdown("#### Pré-visualização do arquivo")
                st.dataframe(df.head(10), use_container_width=True)

                if st.button("Registrar validação no histórico"):
                    registrar_historico_importacao(
                        arquivo.name,
                        resultado,
                        st.session_state.get("user_name", "Usuário não identificado")
                    )
                    st.success("Validação registrada no histórico da sessão.")

            except Exception as e:
                st.error(f"Erro ao processar o arquivo CSV. Detalhes: {e}")
        else:
            st.warning("Nenhum arquivo anexado para validação.")

    with tab_historico:
        st.markdown("### 🧾 Histórico de Importações e Validações")
        st.caption(
            "Histórico temporário das validações realizadas durante a sessão atual. "
            "Este registro auxilia a rastreabilidade operacional do processo de conferência."
        )

        historico = st.session_state.get("historico_importacoes", [])

        if len(historico) == 0:
            st.info("Nenhuma validação foi registrada nesta sessão.")
        else:
            df_historico = pd.DataFrame(historico)
            st.dataframe(df_historico, use_container_width=True, hide_index=True)

            total_validacoes = len(df_historico)
            total_aprovadas = df_historico[df_historico["Status"] == "APROVADO"].shape[0]
            total_alertas = df_historico[df_historico["Status"] == "APROVADO COM ALERTAS"].shape[0]
            total_reprovadas = df_historico[df_historico["Status"] == "REPROVADO"].shape[0]

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Validações", total_validacoes)
            c2.metric("Aprovadas", total_aprovadas)
            c3.metric("Com alertas", total_alertas)
            c4.metric("Reprovadas", total_reprovadas)

            if st.button("Limpar histórico da sessão"):
                st.session_state["historico_importacoes"] = []
                st.rerun()

    with tab_regras:
        st.markdown("### 📌 Regras dos Insumos")
        st.caption(
            "As regras abaixo orientam a preparação dos arquivos utilizados no sistema. "
            "O objetivo é reduzir inconsistências antes da carga dos dados."
        )

        for nome_insumo, config in CONFIG_INSUMOS.items():
            with st.expander(nome_insumo, expanded=False):
                st.write(config["descricao"])

                st.markdown("**Colunas obrigatórias:**")
                st.dataframe(
                    pd.DataFrame({"Coluna": config["colunas"]}),
                    use_container_width=True,
                    hide_index=True
                )

                st.markdown("**Exemplo de preenchimento:**")
                st.dataframe(
                    pd.DataFrame([config["exemplo"]]),
                    use_container_width=True,
                    hide_index=True
                )

        st.markdown("### Recomendações gerais")
        st.write(
            "- Utilizar arquivos no formato CSV.\n"
            "- Manter os cabeçalhos exatamente como no modelo.\n"
            "- Preservar códigos de área com zeros à esquerda, como `000`, `001` e `002`.\n"
            "- Conferir se não há campos obrigatórios vazios.\n"
            "- Validar o arquivo antes da carga oficial no banco.\n"
            "- Evitar alterar manualmente nomes de colunas já padronizadas."
        )


def modulo_sobre_projeto():
    st.markdown('<p class="title-dashboard">ℹ️ Sobre o Projeto</p>', unsafe_allow_html=True)

    st.markdown("### VigiA-SUS — Sistema de Monitoramento Epidemiológico")
    st.write(
        "O VigiA-SUS é uma plataforma acadêmica desenvolvida para apoiar o monitoramento epidemiológico, "
        "organizando dados territoriais, epidemiológicos, climáticos e entomológicos em uma interface única."
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("Versão", "MVP v1.0")
    c2.metric("Área", "Saúde Pública")
    c3.metric("Status", "Funcional")

    st.markdown("---")

    st.markdown("### Objetivo da solução")
    st.write(
        "A proposta do sistema é facilitar a visualização e a análise de dados relevantes para vigilância em saúde, "
        "permitindo consultar áreas monitoradas, acompanhar indicadores de ovitrampas, visualizar dados regionais "
        "e simular cenários de risco epidemiológico."
    )

    st.markdown("### Principais módulos")
    modulos = [
        {
            "Módulo": "Dashboard Preditivo",
            "Finalidade": "Simular cenários de risco e consultar dados regionais epidemiológicos e climáticos."
        },
        {
            "Módulo": "Gestão Territorial",
            "Finalidade": "Consultar áreas monitoradas, indicadores de ovitrampas, cadastrar áreas e realizar manutenção de status."
        },
        {
            "Módulo": "Importação de Insumos",
            "Finalidade": "Validar arquivos CSV antes da carga oficial dos dados no banco PostgreSQL."
        },
        {
            "Módulo": "Login e Perfis",
            "Finalidade": "Controlar o acesso aos módulos conforme perfil do usuário autenticado."
        }
    ]

    st.dataframe(pd.DataFrame(modulos), use_container_width=True, hide_index=True)

    st.markdown("### Equipe e perfis no sistema")
    membros = [
        {"Integrante": "Daniela Teixeira Abreu", "Usuário": "daniela", "Perfil": "Gestor de TI"},
        {"Integrante": "Vinícius Raphael Rios", "Usuário": "vinicius", "Perfil": "Gestor Epidemiológico"},
        {"Integrante": "Matheus Felipe Lopes", "Usuário": "matheus", "Perfil": "Analista de Dados"},
        {"Integrante": "Nátali Isaltino Gomes", "Usuário": "natali", "Perfil": "Operador de Importação"},
        {"Integrante": "Marcela Maria Barbosa", "Usuário": "marcela", "Perfil": "Analista de Vigilância"}
    ]

    st.dataframe(pd.DataFrame(membros), use_container_width=True, hide_index=True)

    st.info(
        "Projeto acadêmico desenvolvido como MVP funcional. O sistema demonstra uma proposta integrada "
        "de apoio ao monitoramento epidemiológico e à organização de dados em saúde pública."
    )


# --- 5. ROTEADOR PRINCIPAL E CONTROLE DE ACESSO ---

if not st.session_state['logged_in']:
    modulo_login()
else:
    role = st.session_state['user_role']
    nome_usuario = st.session_state.get('user_name', '')
    
    with st.sidebar:
        st.markdown("### Sessão")

        if nome_usuario:
            st.info(f"👤 {nome_usuario}\n\nPerfil: {role}")
        else:
            st.info(f"👤 {role}")

        st.markdown("---")
        st.markdown("### Navegação")
        
        opcoes_menu = ["Dashboard Preditivo"]
        
        if role in PERFIS_COM_GESTAO_CONSULTA:
            opcoes_menu.append("Gestão Territorial")

        if role in PERFIS_COM_IMPORTACAO:
            opcoes_menu.append("Importação de Insumos")

        opcoes_menu.append("Sobre o Projeto")
            
        navegacao = st.radio("Módulos do Sistema", opcoes_menu)
        
        st.markdown("---")
        st.markdown("### Conta")
        if st.button("Encerrar Sessão", type="secondary"):
            st.session_state['logged_in'] = False
            st.session_state['user_role'] = ""
            st.session_state['user_name'] = ""
            st.rerun()

    if navegacao == "Dashboard Preditivo":
        modulo_dashboard()
    elif navegacao == "Gestão Territorial":
        modulo_cadastro(role)
    elif navegacao == "Importação de Insumos":
        modulo_importacao()
    elif navegacao == "Sobre o Projeto":
        modulo_sobre_projeto()

    st.markdown("---")
    st.markdown(
        f"<p style='text-align: center; color: #94A3B8; font-size: 12px;'>"
        f"Projeto Acadêmico - Ciência da Computação | VigiA-SUS MVP v1.0 | {datetime.now().year}"
        f"</p>",
        unsafe_allow_html=True
    )