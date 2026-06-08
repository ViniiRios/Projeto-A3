from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

MODEL_FILENAME = "model/vigiasus_xg_model.pkl"

MODEL_FEATURES = [
    "mes",
    "ano",
    "casos_lag1",
    "casos_lag2",
    "TEMP_MEDIA_lag1",
    "TEMP_MEDIA_lag2",
    "PRECIPITACAO_lag1",
    "PRECIPITACAO_lag2",
    "PRESSAO_MEDIA_lag1",
    "PRESSAO_MEDIA_lag2",
]

LIMITE_RISCO_MEDIO = 100.0
LIMITE_RISCO_ALTO = 300.0


def obter_valor(data, chaves, padrao=0.0):
    for chave in chaves:
        if chave in data and data[chave] is not None:
            return data[chave]
    return padrao


def converter_float(valor, padrao=0.0):
    try:
        return float(valor)
    except (TypeError, ValueError):
        return padrao


def limitar(valor, minimo, maximo):
    return max(minimo, min(valor, maximo))


def calcular_taxa_incidencia(casos, populacao):
    if populacao > 0:
        return (casos * 100000.0) / populacao
    return 0.0


def classificar_risco(indice_risco):
    if indice_risco >= LIMITE_RISCO_ALTO:
        return "ALERTA MÁXIMO", "RED"

    if indice_risco >= LIMITE_RISCO_MEDIO:
        return "RISCO MODERADO", "ORANGE"

    return "RISCO BAIXO", "GREEN"


def converter_predicao_modelo(prediction_raw):
    """
    O modelo foi treinado com log1p(casos_total_mes).
    Por isso, a predição bruta precisa voltar para a escala de casos com expm1.
    """
    prediction_raw = float(prediction_raw)

    if prediction_raw < 0:
        return 0.0

    if prediction_raw < 20:
        return float(np.expm1(prediction_raw))

    return prediction_raw


with open(MODEL_FILENAME, "rb") as file:
    xg_model = pickle.load(file)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json() or {}

        print(f"DEBUG - Dados recebidos: {data}")

        mes = converter_float(
            obter_valor(data, ["mes"], 6),
            6
        )

        ano = converter_float(
            obter_valor(data, ["ano"], 2026),
            2026
        )

        casos_lag1 = converter_float(
            obter_valor(data, ["casos_lag1", "numeroCasos", "notificacoes_atual"], 0),
            0
        )

        casos_lag2 = converter_float(
            obter_valor(data, ["casos_lag2", "casosLag2", "notificacoes_anterior"], 0),
            0
        )

        temp_lag1 = converter_float(
            obter_valor(data, ["TEMP_MEDIA_lag1", "temperatura"], 25.0),
            25.0
        )

        temp_lag2 = converter_float(
            obter_valor(data, ["TEMP_MEDIA_lag2"], temp_lag1 - 2),
            temp_lag1 - 2
        )

        precipitacao_lag1 = converter_float(
            obter_valor(data, ["PRECIPITACAO_lag1", "chuva"], 0.0),
            0.0
        )

        precipitacao_lag2 = converter_float(
            obter_valor(data, ["PRECIPITACAO_lag2"], precipitacao_lag1 - 50),
            precipitacao_lag1 - 50
        )

        pressao_lag1 = converter_float(
            obter_valor(data, ["PRESSAO_MEDIA_lag1"], 900.0),
            900.0
        )

        pressao_lag2 = converter_float(
            obter_valor(data, ["PRESSAO_MEDIA_lag2"], 900.5),
            900.5
        )

        populacao = converter_float(
            obter_valor(data, ["populacao"], 200000),
            200000
        )

        # Limites para evitar valores absurdos fora do padrão do modelo.
        temp_lag1 = limitar(temp_lag1, 15.0, 30.0)
        temp_lag2 = limitar(temp_lag2, 15.0, 30.0)

        precipitacao_lag1 = max(precipitacao_lag1, 0.0)
        precipitacao_lag2 = max(precipitacao_lag2, 0.0)

        pressao_lag1 = limitar(pressao_lag1, 890.0, 910.0)
        pressao_lag2 = limitar(pressao_lag2, 890.0, 910.0)

        dados_modelo = {
            "mes": mes,
            "ano": ano,
            "casos_lag1": casos_lag1,
            "casos_lag2": casos_lag2,
            "TEMP_MEDIA_lag1": temp_lag1,
            "TEMP_MEDIA_lag2": temp_lag2,
            "PRECIPITACAO_lag1": precipitacao_lag1,
            "PRECIPITACAO_lag2": precipitacao_lag2,
            "PRESSAO_MEDIA_lag1": pressao_lag1,
            "PRESSAO_MEDIA_lag2": pressao_lag2,
        }

        input_df = pd.DataFrame([dados_modelo], columns=MODEL_FEATURES)
        input_df = input_df.fillna(0).astype(float)

        prediction_raw = xg_model.predict(input_df)[0]
        casos_previstos_modelo = converter_predicao_modelo(prediction_raw)

        taxa_atual = calcular_taxa_incidencia(casos_lag1, populacao)
        taxa_prevista_modelo = calcular_taxa_incidencia(casos_previstos_modelo, populacao)

        indice_risco = max(taxa_atual, taxa_prevista_modelo)

        nivel, cor = classificar_risco(indice_risco)

        print("DEBUG - Dados usados pelo modelo:")
        print(dados_modelo)
        print(f"DEBUG - Predição bruta do modelo: {prediction_raw}")
        print(f"DEBUG - Casos previstos pelo modelo: {casos_previstos_modelo}")
        print(f"DEBUG - Taxa atual: {taxa_atual}")
        print(f"DEBUG - Taxa prevista pelo modelo: {taxa_prevista_modelo}")
        print(f"DEBUG - Índice de risco usado: {indice_risco} ({nivel})")

        return jsonify({
            "taxaIncidencia": float(indice_risco),
            "taxaAtual": float(taxa_atual),
            "taxaPrevistaModelo": float(taxa_prevista_modelo),
            "casosPrevistosModelo": float(casos_previstos_modelo),
            "indiceRiscoConsiderado": float(indice_risco),
            "risco": str(nivel),
            "corAlerta": str(cor),
            "status": "sucesso"
        })

    except Exception as e:
        import traceback
        print(f"ERRO CRÍTICO NO PYTHON:\n{traceback.format_exc()}")
        return jsonify({"erro": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)