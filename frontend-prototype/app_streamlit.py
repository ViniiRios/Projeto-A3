import streamlit as st
import requests
from datetime import datetime

# --- 1. CONFIGURAÇÃO DA PÁGINA ---

st.set_page_config(page_title="VigiA-SUS: Monitoramento BH", layout="wide")

# --- 2. ESTILIZAÇÃO CSS CUSTOMIZADA ---

st.markdown("""
    <style>
    .stSuccess {
        background-color: #FFFFFF;
        border-left: 6px solid #4CAF50;
        color: #000000;
        padding: 10px;
        border-radius: 5px;
    }
    h3 {
        color: #3CB371; 
        border-bottom: 2px solid #3CB371;
        padding-bottom: 5px;
    }
    div.stButton > button {
        background-color: #4CAF50; 
        color: white; 
        width: 100%;
        font-weight: bold;
        border-radius: 8px; 
        height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL (ENTRADAS DE DADOS) ---

st.sidebar.header("🧭 Parâmetros de Entrada")
predict_date = st.sidebar.date_input("Mês da Análise", datetime(2025, 12, 1))

st.sidebar.markdown("---")
st.sidebar.subheader("📈 Histórico Epidemiológico")

casos_lag1 = st.sidebar.number_input(
    "Casos (Mês Atual/Base)", 
    min_value=0, 
    max_value=100000, 
    value=500, 
    step=1,
    help="Insira o número exato de casos confirmados neste mês."
)

casos_lag2 = st.sidebar.number_input(
    "Casos (Mês Anterior)", 
    min_value=0, 
    max_value=100000, 
    value=300, 
    step=1,
    help="Insira o número de casos registrados no mês passado."
)

populacao = st.sidebar.number_input(
    "População da Área", 
    min_value=1, 
    value=2500000, 
    step=100
)

st.sidebar.markdown("---")
st.sidebar.subheader("☁️ Previsão Climática")
temp_input = st.sidebar.number_input("Temperatura Média (°C)", value=25.0, step=0.1)
precip_input = st.sidebar.number_input("Precipitação (mm)", value=150.0, step=0.1)

# --- 4. PAINEL PRINCIPAL (VISUALIZAÇÃO) ---

st.title("Sistema Preditivo VigiA-SUS 🦠")
st.markdown(f"Painel de Validação para **Belo Horizonte**. Referência: **{predict_date.strftime('%B/%Y')}**")

with st.container():
    st.markdown("### Resumo dos Dados Selecionados")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Temperatura", f"{temp_input}°C")
    c2.metric("Precipitação", f"{precip_input}mm")
    c3.metric("Casos Base", casos_lag1)
    c4.metric("População", f"{populacao:,}".replace(",", "."))

st.markdown("---")

# --- 5. BLOCO DE EXECUÇÃO (FORMULÁRIO E INTEGRAÇÃO JAVA) ---

with st.form("main_prediction_form"):
    st.info("Clique no botão abaixo para enviar os dados ao Backend Java e processar a IA.")
    
    submitted = st.form_submit_button("GERAR PREVISÃO VIA BACKEND JAVA")

if submitted:
    url_java = "http://localhost:8080/api/areas/calcular-risco"

    payload = {
        "temperatura": temp_input,
        "chuva": precip_input,
        "numeroCasos": casos_lag1,
        "casosLag2": casos_lag2,
        "populacao": populacao,
        "mes": predict_date.month,
        "ano": predict_date.year
    }

    with st.spinner("🚀 Integrando com Java Spring Boot & Motor de IA..."):
        try:
            response = requests.post(url_java, json=payload, timeout=15)

            if response.status_code == 200:
                dados_retorno = response.json()
                
                nivel_risco = dados_retorno.get('risco', 'N/A').upper()
                incidencia = dados_retorno.get('taxaIncidencia', 0.0)

                cores = {
                    "ALERTA MÁXIMO": "#FF4B4B", 
                    "RISCO MODERADO": "#FFA500", 
                    "RISCO BAIXO": "#2E7D32"
                }
                cor_display = cores.get(nivel_risco, "#1F77B4")

                st.markdown("### 📋 Status de Risco Identificado:")
                st.markdown(
                    f'<h1 style="color:{cor_display}; font-size:54px; text-align: center; border: 2px solid {cor_display}; border-radius: 15px; padding: 10px;">'
                    f'{nivel_risco}</h1>', 
                    unsafe_allow_html=True
                )
                
                st.write("")
                st.success(f"## 📊 Taxa de Incidência: **{incidencia:.2f}**")
                st.caption("Cálculo realizado com base nos modelos epidemiológicos integrados.")

            elif response.status_code == 400:
                st.error("❌ Erro 400: O Java recusou os dados. Verifique se os valores são válidos.")
            else:
                st.error(f"⚠️ Erro no servidor Java: Status {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("🔌 Erro de Conexão: O Backend Java (porta 8080) não respondeu. Ele está ligado?")
        except Exception as e:
            st.error(f"❌ Ocorreu um erro inesperado: {e}")

# --- 6. RODAPÉ ---

st.markdown("---")
st.caption(f"Protótipo de Validação - VigiaSUS | Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")