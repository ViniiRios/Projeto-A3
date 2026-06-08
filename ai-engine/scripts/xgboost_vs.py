import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor


# ============================================================
# Treinamento do modelo preditivo VigiA-SUS
# Base esperada:
# ai-engine/dados/tratados/base_final_etapa1.csv
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

ARQUIVO_BASE = BASE_DIR / "dados" / "tratados" / "base_final_etapa1.csv"
PASTA_MODELO = BASE_DIR / "model"
PASTA_SAIDA = BASE_DIR / "dados" / "tratados"

ARQUIVO_MODELO = PASTA_MODELO / "vigiasus_xg_model.pkl"
ARQUIVO_COMPARACAO = PASTA_SAIDA / "model_comparison.csv"
ARQUIVO_PREVISOES = PASTA_SAIDA / "previsao_arboviroses_xg.csv"


FEATURES = [
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


def converter_numero(valor):
    """
    Converte números vindos de CSV brasileiro ou americano.

    Exemplos aceitos:
    - "21,95"  -> 21.95
    - "21.95"  -> 21.95
    - "1.234,56" -> 1234.56
    - "1234.56" -> 1234.56
    - 21.95 -> 21.95

    Importante:
    Não remove ponto decimal quando o valor já veio como 21.95.
    Esse era o erro anterior que transformava 21.95 em 2195.
    """

    if pd.isna(valor):
        return np.nan

    if isinstance(valor, (int, float, np.integer, np.floating)):
        return float(valor)

    texto = str(valor).strip()
    texto = texto.replace('"', "").replace("'", "")
    texto = texto.replace(" ", "")

    if texto == "":
        return np.nan

    # Caso brasileiro com milhar e decimal: 1.234,56
    if "." in texto and "," in texto:
        texto = texto.replace(".", "")
        texto = texto.replace(",", ".")

    # Caso brasileiro simples: 21,95
    elif "," in texto:
        texto = texto.replace(",", ".")

    # Caso americano: 21.95
    # Não mexe no ponto.

    return float(texto)


def ler_base_final(caminho_arquivo):
    """
    Lê a base final como texto primeiro, para evitar que o pandas
    interprete vírgula/ponto de forma errada.
    """

    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    try:
        df = pd.read_csv(caminho_arquivo, sep=None, engine="python", dtype=str)
    except Exception:
        try:
            df = pd.read_csv(caminho_arquivo, sep=";", dtype=str)
        except Exception:
            df = pd.read_csv(caminho_arquivo, sep=",", dtype=str)

    df.columns = [str(coluna).strip() for coluna in df.columns]

    colunas_obrigatorias = [
        "data",
        "TEMP_MEDIA",
        "PRECIPITACAO",
        "PRESSAO_MEDIA",
        "casos_total_mes",
    ]

    for coluna in colunas_obrigatorias:
        if coluna not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente na base final: {coluna}")

    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    for coluna in ["TEMP_MEDIA", "PRECIPITACAO", "PRESSAO_MEDIA"]:
        df[coluna] = df[coluna].apply(converter_numero)

    df["casos_total_mes"] = df["casos_total_mes"].apply(converter_numero).round().astype(int)

    if df["data"].isna().any():
        raise ValueError("Existem datas inválidas na base final.")

    if df[["TEMP_MEDIA", "PRECIPITACAO", "PRESSAO_MEDIA", "casos_total_mes"]].isna().any().any():
        raise ValueError("Existem valores numéricos inválidos na base final.")

    df = df.sort_values("data").reset_index(drop=True)

    return df


def preparar_features(df):
    df = df.copy()

    df["mes"] = df["data"].dt.month
    df["ano"] = df["data"].dt.year

    df["casos_lag1"] = df["casos_total_mes"].shift(1)
    df["casos_lag2"] = df["casos_total_mes"].shift(2)

    df["TEMP_MEDIA_lag1"] = df["TEMP_MEDIA"].shift(1)
    df["TEMP_MEDIA_lag2"] = df["TEMP_MEDIA"].shift(2)

    df["PRECIPITACAO_lag1"] = df["PRECIPITACAO"].shift(1)
    df["PRECIPITACAO_lag2"] = df["PRECIPITACAO"].shift(2)

    df["PRESSAO_MEDIA_lag1"] = df["PRESSAO_MEDIA"].shift(1)
    df["PRESSAO_MEDIA_lag2"] = df["PRESSAO_MEDIA"].shift(2)

    df = df.dropna().reset_index(drop=True)

    if df.empty:
        raise ValueError("A base ficou vazia após criação dos lags. Verifique os dados de entrada.")

    return df


def treinar_modelos(df_modelo):
    x = df_modelo[FEATURES]
    y_real = df_modelo["casos_total_mes"]

    # Transformação logarítmica para reduzir impacto de picos muito altos.
    y_treino_modelo = np.log1p(y_real)

    # Separação temporal simples: últimos 3 meses para teste.
    tamanho_teste = min(3, max(1, len(df_modelo) // 5))

    x_train = x.iloc[:-tamanho_teste]
    x_test = x.iloc[-tamanho_teste:]

    y_train = y_treino_modelo.iloc[:-tamanho_teste]
    y_test_real = y_real.iloc[-tamanho_teste:]

    modelos = {
        "XGBoost": XGBRegressor(
            objective="reg:squarederror",
            n_estimators=80,
            max_depth=2,
            learning_rate=0.05,
            subsample=0.9,
            colsample_bytree=0.9,
            random_state=42,
        ),
        "Regressao Linear": LinearRegression(),
        "MLPRegressor": MLPRegressor(
            hidden_layer_sizes=(16,),
            max_iter=2000,
            random_state=42,
        ),
    }

    resultados = []
    previsoes_xgboost = None
    modelo_xgboost = None

    for nome, modelo in modelos.items():
        modelo.fit(x_train, y_train)

        pred_log = modelo.predict(x_test)
        pred_real = np.expm1(pred_log)
        pred_real = np.maximum(pred_real, 0)

        rmse = mean_squared_error(y_test_real, pred_real) ** 0.5

        resultados.append({
            "modelo": nome,
            "rmse": round(float(rmse), 4),
        })

        if nome == "XGBoost":
            previsoes_xgboost = pred_real
            modelo_xgboost = modelo

    df_resultados = pd.DataFrame(resultados).sort_values("rmse")

    df_previsoes = df_modelo.iloc[-tamanho_teste:][[
        "data",
        "casos_total_mes",
        "TEMP_MEDIA",
        "PRECIPITACAO",
        "PRESSAO_MEDIA",
    ]].copy()

    df_previsoes["previsao_xgboost"] = np.round(previsoes_xgboost, 2)
    df_previsoes["erro_absoluto"] = np.round(
        abs(df_previsoes["casos_total_mes"] - df_previsoes["previsao_xgboost"]),
        2
    )

    return modelo_xgboost, df_resultados, df_previsoes


def salvar_resultados(modelo, df_resultados, df_previsoes):
    PASTA_MODELO.mkdir(parents=True, exist_ok=True)
    PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

    with open(ARQUIVO_MODELO, "wb") as arquivo:
        pickle.dump(modelo, arquivo)

    df_resultados.to_csv(ARQUIVO_COMPARACAO, index=False, sep=";")
    df_previsoes.to_csv(ARQUIVO_PREVISOES, index=False, sep=";")

    print("\nModelo salvo em:")
    print(ARQUIVO_MODELO)

    print("\nComparação dos modelos salva em:")
    print(ARQUIVO_COMPARACAO)

    print("\nPrevisões de teste salvas em:")
    print(ARQUIVO_PREVISOES)


def main():
    print("Lendo base final:")
    print(ARQUIVO_BASE)

    df = ler_base_final(ARQUIVO_BASE)

    print("\nResumo da base carregada:")
    print(df.head())

    print("\nLinhas:", len(df))
    print("Período:", df["data"].min().date(), "até", df["data"].max().date())
    print("Total de casos:", int(df["casos_total_mes"].sum()))

    print("\nVerificação dos valores climáticos:")
    print(df[["TEMP_MEDIA", "PRECIPITACAO", "PRESSAO_MEDIA"]].describe())

    if df["casos_total_mes"].sum() == 0:
        raise ValueError("A base final está com casos_total_mes zerado. O modelo não deve ser treinado assim.")

    df_modelo = preparar_features(df)

    print("\nBase após criação de lags:")
    print(df_modelo[["data", "casos_total_mes"] + FEATURES].head())
    print("\nLinhas úteis para treino/teste:", len(df_modelo))

    modelo, df_resultados, df_previsoes = treinar_modelos(df_modelo)

    print("\nComparação dos modelos:")
    print(df_resultados)

    print("\nPrevisões XGBoost nos meses de teste:")
    print(df_previsoes)

    salvar_resultados(modelo, df_resultados, df_previsoes)

    print("\nTreinamento concluído com sucesso.")


if __name__ == "__main__":
    main()