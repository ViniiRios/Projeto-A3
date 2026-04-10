from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
from pathlib import Path

app = Flask(__name__)

# --- CONFIGURAÇÕES DO MODELO (Extraído do seu Streamlit) ---
MODEL_FILENAME = "model/vigiasus_xg_model.pkl"
MODEL_FEATURES = [
    'mes', 'ano', 'casos_lag1', 'casos_lag2',
    'TEMP_MEDIA_lag1', 'TEMP_MEDIA_lag2',
    'PRECIPITACAO_lag1', 'PRECIPITACAO_lag2',
    'PRESSAO_MEDIA_lag1', 'PRESSAO_MEDIA_lag2'
]

# Constantes de Risco (Mantendo o padrão do seu projeto)
LIMITE_RISCO_ALTO = 2000
LIMITE_RISCO_MEDIO = 800

# Carregar o modelo uma única vez ao iniciar o servidor
with open(MODEL_FILENAME, 'rb') as file:
    xg_model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Recebe os dados do Java
        dados_entrada = request.get_json()
        
        # 2. Converte para DataFrame garantindo a ordem das colunas
        input_df = pd.DataFrame([dados_entrada], columns=MODEL_FEATURES)
        
        # 3. Predição
        prediction = xg_model.predict(input_df)[0]
        
        # 4. Lógica de "Zero Lock" (Ajuste que você tinha no Streamlit)
        if prediction < 5.0:
            prediction = (input_df['TEMP_MEDIA_lag1'].iloc[0] * 50) + (input_df['PRECIPITACAO_lag1'].iloc[0] * 1)
        
        # 5. Classificação de Risco
        if prediction >= LIMITE_RISCO_ALTO:
            nivel = "ALERTA MÁXIMO"
            cor = "RED"
        elif prediction >= LIMITE_RISCO_MEDIO:
            nivel = "RISCO MODERADO"
            cor = "ORANGE"
        else:
            nivel = "RISCO BAIXO"
            cor = "GREEN"

        return jsonify({
            'casos_previstos': int(round(prediction, 0)),
            'nivel_risco': nivel,
            'cor_alerta': cor,
            'status': 'sucesso'
        })

    except Exception as e:
        return jsonify({'erro': f"Falha na predição: {str(e)}"}), 400

if __name__ == '__main__':
    # Roda na porta 5000 para não conflitar com o Java (8080)
    app.run(host='0.0.0.0', port=5000, debug=True)