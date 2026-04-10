import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
import pickle
import warnings
import os
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Suprime o UserWarning de indexação que pode aparecer
warnings.filterwarnings("ignore", category=UserWarning)

# Constantes do Modelo
FILE_PATH = "dados/tratados/base_final_etapa1.csv"
SEED = 42
CLIMATE_COLS = ['TEMP_MEDIA', 'PRECIPITACAO', 'PRESSAO_MEDIA']
LAG_PERIODS = [1, 2]

# --- 1. CARREGAMENTO E FEATURE ENGINEERING ---
try:
    df = pd.read_csv(FILE_PATH, sep=';', parse_dates=['data'])
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}!")
    print(f"Verifique se o arquivo {FILE_PATH} foi criado pelo main.py.")
    exit()

# A. Features Temporais
df['mes'] = df['data'].dt.month
df['ano'] = df['data'].dt.year

# B. Lags (Defasagens) - CRÍTICO para Séries Temporais
for lag in LAG_PERIODS:
    df[f'casos_lag{lag}'] = df['casos_total_mes'].shift(lag)

for col in CLIMATE_COLS:
    for lag in LAG_PERIODS:
        df[f'{col}_lag{lag}'] = df[col].shift(lag)

df.dropna(inplace=True)

# --- 2. SELEÇÃO DE FEATURES E PREPARAÇÃO ---
Y_raw = df['casos_total_mes']

# TRANSFORMAÇÃO LOGARÍTMICA (ln(Y+1))
Y = np.log1p(Y_raw)

FEATURES = ['mes', 'ano'] + [col for col in df.columns if '_lag' in col]
X = df[FEATURES]

# --- 3. DIVISÃO EM TREINO E TESTE ---
TEST_SIZE = 3
X_train = X.iloc[:-TEST_SIZE]
X_test = X.iloc[-TEST_SIZE:]
Y_train = Y.iloc[:-TEST_SIZE] # Treino em Log
Y_test = Y.iloc[-TEST_SIZE:] # Teste em Log (em log)

print(f"Treinamento: {X_train.shape[0]} meses")
print(f"Teste: {X_test.shape[0]} meses")

# --- 4. TREINAMENTO DO MODELO XGBOOST E OS OUTROS ---
print("\nIniciando treinamento dos 3 Modelos...")

# 1. XGBoost (Modelo Boosting - Máxima performance)
xgb_model = XGBRegressor(n_estimators=100, random_state=SEED, n_jobs=-1, max_depth=5, learning_rate=0.1)
xgb_model.fit(X_train, Y_train)
Y_pred_xgb_log = xgb_model.predict(X_test)
rmse_xgb = np.sqrt(mean_squared_error(np.expm1(Y_test), np.expm1(Y_pred_xgb_log)))
print(f"XGBoost RMSE: {rmse_xgb:.2f}")

# 2. Regressão Linear (Modelo Clássico - Baseline)
lin_model = LinearRegression()
lin_model.fit(X_train, Y_train)
Y_pred_lin_log = lin_model.predict(X_test)
rmse_lin = np.sqrt(mean_squared_error(np.expm1(Y_test), np.expm1(Y_pred_lin_log)))
print(f"Linear Regression RMSE: {rmse_lin:.2f}")

# 3. MLPRegressor (Rede Neural)
mlp_model = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=200, random_state=SEED)
mlp_model.fit(X_train, Y_train)
Y_pred_mlp_log = mlp_model.predict(X_test)
rmse_mlp = np.sqrt(mean_squared_error(np.expm1(Y_test), np.expm1(Y_pred_mlp_log)))
print(f"MLP Regressor RMSE: {rmse_mlp:.2f}")


# --- 5. AVALIAÇÃO E PREVISÃO (Foco no XGBoost) ---
Y_pred_log = Y_pred_xgb_log
Y_pred = np.expm1(Y_pred_log)
Y_real = np.expm1(Y_test)

# Calcula o RMSE no valor real (sem log)
rmse = rmse_xgb

print(f"\nResultados da Avaliação:")
print(f"RMSE (Root Mean Squared Error): {rmse:.2f} casos")

# --- 6. SALVAR O MODELO TREINADO ---
with open('vigiasus_xg_model.pkl', 'wb') as file:
    pickle.dump(xgb_model, file)
print("✅ Modelo XG salvo.")

# --- 7. IMPORTÂNCIA DAS FEATURES ---
feature_importances = pd.Series(xgb_model.feature_importances_, index=X.columns)
print("\nImportância das Features no Modelo (VigiA-SUS):")
print(feature_importances.sort_values(ascending=False).to_string())

# --- 8. SALVAR RESULTADOS DA PREVISÃO E COMPARAÇÃO ---
RESULTS_PATH = "dados/tratados/previsao_arboviroses_xg.csv"

# Cria DataFrame para salvar as previsões do modelo principal (XGBoost)
resultados_df = pd.DataFrame({
    'Data': df['data'].iloc[-TEST_SIZE:].reset_index(drop=True).tolist(),
    'Real': Y_real.round(0),
    'Previsto': Y_pred.round(0)
})

resultados_df.to_csv(RESULTS_PATH, index=False, sep=';')
print(f"\n✅ Resultados da Previsão salvos em: {RESULTS_PATH}")

# Criando o DataFrame de Comparação de Modelos (Requisito do relatório)
model_results = pd.DataFrame({
    'Modelo': ['XGBoost (Boosting)', 'MLPRegressor (Rede Neural)', 'Regressão Linear (Baseline)'],
    'RMSE (Erro em Casos)': [rmse_xgb, rmse_mlp, rmse_lin]
})

COMPARISON_PATH = "dados/tratados/model_comparison.csv"
model_results.to_csv(COMPARISON_PATH, index=False, sep=';')
print(f"✅ Tabela de comparação salva em: {COMPARISON_PATH}")

print("\nPrevisões vs. Valores Reais (Últimos 3 meses de teste):")
print(resultados_df.to_string())