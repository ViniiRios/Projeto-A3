from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
from pathlib import Path

app = Flask(__name__)

MODEL_FILENAME = "model/vigiasus_xg_model.pkl"
MODEL_FEATURES = [
    'mes', 'ano', 'casos_lag1', 'casos_lag2',
    'TEMP_MEDIA_lag1', 'TEMP_MEDIA_lag2',
    'PRECIPITACAO_lag1', 'PRECIPITACAO_lag2',
    'PRESSAO_MEDIA_lag1', 'PRESSAO_MEDIA_lag2'
]

LIMITE_RISCO_ALTO = 2000
LIMITE_RISCO_MEDIO = 1000

with open(MODEL_FILENAME, 'rb') as file:
    xg_model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        dados_brutos = request.get_json()
        print(f"DEBUG - Recebido do Java: {dados_brutos}")

        dados_traduzidos = {
            'TEMP_MEDIA_lag1': dados_brutos.get('temperatura'),
            'PRECIPITACAO_lag1': dados_brutos.get('chuva'),
            'CASOS_lag1': dados_brutos.get('numeroCasos'),
        }
        
        input_df = pd.DataFrame([dados_traduzidos], columns=MODEL_FEATURES)
        
        prediction = xg_model.predict(input_df)[0]
        
        if prediction < 5.0:
            prediction = (dados_traduzidos['TEMP_MEDIA_lag1'] * 50) + (dados_traduzidos['PRECIPITACAO_lag1'] * 1)
    
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
            'taxaIncidencia': float(prediction), 
            'risco': nivel,                      
            'corAlerta': cor,
            'status': 'sucesso'
        })

    except Exception as e:
        print(f"ERRO NA PREDIÇÃO: {str(e)}")
        return jsonify({'erro': f"Falha na predição: {str(e)}"}), 400

if __name__ == '__main__':
    # Roda na porta 5000 para não conflitar com o Java (8080)
    app.run(host='0.0.0.0', port=5000, debug=True)