import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="VigiA-SUS: Monitoramento BH", layout="wide")

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
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.header("Parâmetros de Entrada")

predict_date = st.sidebar.date_input("Mês da Análise", datetime(2025, 12, 1))

st.sidebar.markdown("---")
st.sidebar.subheader("Histórico Epidemiológico")
casos_lag1 = st.sidebar.slider("Casos (Mês Anterior)", 0, 2000, 500)
casos_lag2 = st.sidebar.slider("Casos (2 Meses Anteriores)", 0, 2000, 300)

st.sidebar.markdown("---")
st.sidebar.subheader("Previsão Climática")
temp_input = st.sidebar.number_input("Temperatura Média (°C)", value=25.0, step=0.1)
precip_input = st.sidebar.number_input("Precipitação (mm)", value=150.0, step=0.1)

st.title("Sistema Preditivo VigiA-SUS 🦠")
st.markdown(f"Painel de Validação para **Belo Horizonte**. Mês de referência: **{predict_date.strftime('%B/%Y')}**")

with st.form("main_prediction_form"):
    st.markdown("### Confirmar Dados para Cálculo de Risco")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperatura", f"{temp_input}°C")
    col2.metric("Precipitação", f"{precip_input}mm")
    col3.metric("Casos Base", casos_lag1)

    submitted = st.form_submit_button("GERAR PREVISÃO VIA BACKEND JAVA")

    if submitted:
        payload = {
            "temperatura": temp_input,
            "chuva": precip_input,
            "numeroCasos": casos_lag1,
            "casosLag2": casos_lag2,
            "populacao": 2500000,
            "mes": predict_date.month,
            "ano": predict_date.year
        }

        with st.spinner("Integrando com Java Spring Boot & Motor de IA..."):
            try:
                response = requests.post(
                    "http://localhost:8080/api/areas/calcular-risco", 
                    json=payload,
                    timeout=10
                )

                if response.status_code == 200:
                    dados_retorno = response.json()
                    
                    nivel_risco = dados_retorno.get('risco', 'N/A').upper()
                    incidencia = dados_retorno.get('taxaIncidencia', 0)

                    cores = {"ALERTA MÁXIMO": "red", "RISCO MODERADO": "orange", "RISCO BAIXO": "green"}
                    cor = cores.get(nivel_risco, "blue")

                    st.markdown(f"### Status de Risco Identificado:")
                    st.markdown(f'<h1 style="color:{cor}; font-size:48px; text-align: center;">{nivel_risco}</h1>', 
                                unsafe_allow_html=True)
                    
                    st.success(f"## 📊 {int(incidencia)} Casos Previstos (Taxa de Incidência)")
                    
                elif response.status_code == 400:
                    st.error("Erro 400: O Java barrou os dados. Verifique os limites permitidos.")
                else:
                    st.error(f"Erro no servidor: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("❌ Erro de Conexão: O Backend Java (8080) está offline.")
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")

st.markdown("---")
st.caption("Protótipo de Validação - Sistema VigiaSUS")