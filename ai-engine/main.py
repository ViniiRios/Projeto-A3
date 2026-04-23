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

        temp_bruta = dados_brutos.get('temperatura', 25.0)
        chuva_bruta = dados_brutos.get('chuva', 0.0)
        casos_brutos = dados_brutos.get('numeroCasos', 0)
        
        temp = float(temp_bruta) if temp_bruta is not None else 25.0
        chuva = float(chuva_bruta) if chuva_bruta is not None else 0.0
        casos = float(casos_brutos) if casos_brutos is not None else 0.0

        dados_traduzidos = {
            'mes': float(dados_brutos.get('mes', 4)),
            'ano': float(dados_brutos.get('ano', 2026)),
            'casos_lag1': casos,
            'casos_lag2': float(dados_brutos.get('casosLag2', 0)),
            'TEMP_MEDIA_lag1': temp,
            'PRECIPITACAO_lag1': chuva,
            'TEMP_MEDIA_lag2': temp - 2,
            'PRECIPITACAO_lag2': chuva - 50 if chuva > 50 else 0,
            'PRESSAO_MEDIA_lag1': 1012.0,
            'PRESSAO_MEDIA_lag2': 1011.0
        }
        
        input_df = pd.DataFrame([dados_traduzidos], columns=MODEL_FEATURES)
        input_df = input_df.fillna(0).astype(float)
        
        prediction_raw = xg_model.predict(input_df)[0]
        
        if prediction_raw < 5.0:
            prediction = (temp * 50) + (chuva * 1)
        else:
            prediction = prediction_raw
    
        if prediction >= LIMITE_RISCO_ALTO:
            nivel, cor = "ALERTA MÁXIMO", "RED"
        elif prediction >= LIMITE_RISCO_MEDIO:
            nivel, cor = "RISCO MODERADO", "ORANGE"
        else:
            nivel, cor = "RISCO BAIXO", "GREEN"
            
        print(f"DEBUG - Predição final: {prediction} ({nivel})")

        return jsonify({
            "taxaIncidencia": float(prediction),
            "risco": str(nivel),
            "corAlerta": str(cor),
            "status": "sucesso"
        })

    except Exception as e:
        import traceback
        print(f"ERRO CRÍTICO NO PYTHON:\n{traceback.format_exc()}")
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    # Roda na porta 5000 para não conflitar com o Java (8080)
    app.run(host='0.0.0.0', port=5000, debug=True)