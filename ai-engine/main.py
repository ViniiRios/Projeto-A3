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

LIMITE_RISCO_MEDIO = 100.0
LIMITE_RISCO_ALTO = 300.0

with open(MODEL_FILENAME, 'rb') as file:
    xg_model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    print(f"DEBUG BRUTO: {data}")

    # Tenta pegar o valor de casos de qualquer uma dessas chaves
    casos = data.get('casos_lag1') or data.get('numeroCasos') or data.get('notificacoes_atual') or 0
    
    # Tenta pegar a população
    populacao = data.get('populacao') or 200000
    
    # Converte para float para garantir que a conta não zere
    casos = float(casos)
    populacao = float(populacao)

    # CÁLCULO DA TAXA (AQUI NÃO TEM ERRO)
    if populacao > 0:
        taxa_calculada = (casos * 100000.0) / populacao
    else:
        taxa_calculada = 0.0

    print(f"DEBUG CALCULO: Casos: {casos}, Pop: {populacao}, Taxa: {taxa_calculada}")

    try:
        print(f"DEBUG - Recebido: {data}")

        temp_bruta = data.get('temperatura', 25.0)
        chuva_bruta = data.get('chuva', 0.0)
        casos_brutos = data.get('numeroCasos', 0)
        notificacoes_atual = int(data.get('casos_lag1', 0))
        populacao = int(data.get('populacao', 200000))

        temp = float(temp_bruta) if temp_bruta is not None else 25.0
        chuva = float(chuva_bruta) if chuva_bruta is not None else 0.0
        casos = float(casos_brutos) if casos_brutos is not None else 0.0

        dados_traduzidos = {
            'mes': float(data.get('mes', 4)),
            'ano': float(data.get('ano', 2026)),
            'casos_lag1': casos,
            'casos_lag2': float(data.get('casosLag2', 0)),
            'TEMP_MEDIA_lag1': temp,
            'PRECIPITACAO_lag1': chuva,
            'TEMP_MEDIA_lag2': temp - 2,
            'PRECIPITACAO_lag2': chuva - 50 if chuva > 50 else 0,
            'PRESSAO_MEDIA_lag1': 1012.0,
            'PRESSAO_MEDIA_lag2': 1011.0
        }
        
        input_df = pd.DataFrame([dados_traduzidos], columns=MODEL_FEATURES)
        input_df = input_df.fillna(0).astype(float)
        
        prediction = 0.0

        prediction_raw = xg_model.predict(input_df)[0]
        
        if populacao > 0:
            taxa_calculada = (notificacoes_atual / populacao) * 100000
        else:
            taxa_calculada = 0.0

        if prediction_raw < 5.0:
            prediction = taxa_calculada
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