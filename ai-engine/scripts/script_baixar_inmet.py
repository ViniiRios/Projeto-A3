import pandas as pd
from pathlib import Path


def get_dados_inmet_local(pasta="dados/dados_brutos"):
    """
    Lê e combina dados meteorológicos mensais do INMET (A521 e F501),
    usando a detecção flexível dos nomes de colunas de medição mensal.
    (Corrigido engine='python' e skiprows=10 para resolver tokenização).
    """

    # Lista todos os arquivos CSV do INMET na pasta de dados brutos
    arquivos = list(Path(pasta).glob("inmet_*.csv"))
    if not arquivos:
        print("⚠️ Nenhum arquivo INMET encontrado.")
        return pd.DataFrame()

    dfs = [] # Lista para armazenar DataFrames limpos de cada estação

    for arq in arquivos:
        print(f"📡 Lendo {arq.name} ...")

        try:
            # --- 1. Leitura: Configurações de leitura robusta para dados abertos do INMET ---
            # engine='python' (mais robusto), skiprows=10 (pula metadados) e quotechar='"'
            df = pd.read_csv(arq, sep=';', encoding='utf-8', engine='python', skiprows=10, quotechar='"')

            # --- 2. DETECÇÃO FLEXÍVEL DE COLUNAS ---
            col_data = df.columns[0].strip() # Assume que a primeira coluna é a data

            # --- Correção de Flexibilidade ---
            def find_col(keyword1, keyword2):
                """Busca colunas que contenham AMBAS as palavras-chave em MAIÚSCULO."""
                return next((c for c in df.columns if keyword1 in c.upper() and keyword2 in c.upper()), None)

            # Detecta colunas de forma flexível para ignorar acentos/espaços
            col_temp_media = find_col('TEMPERATURA', 'MEDIA')
            col_precip_total = find_col('PRECIPITACAO', 'TOTAL')
            col_pressao = find_col('PRESSAO', 'MEDIA')

            # Se as colunas essenciais não forem encontradas, o arquivo é ignorado
            if not col_temp_media or not col_precip_total:
                print(f"⚠️ {arq.name} ignorado: Colunas essenciais de clima não encontradas.")
                continue

            # --- 3. Conversão e Limpeza ---

            # Converte a coluna de data para o formato datetime
            df[col_data] = pd.to_datetime(df[col_data], errors='coerce')
            df = df.dropna(subset=[col_data])
            # Filtra apenas o período de interesse (2022-2023)
            df = df[(df[col_data] >= '2022-01-01') & (df[col_data] <= '2023-12-31')].copy()

            # Trata vírgula decimal e converte para numérico
            def clean_and_convert(series):
                return pd.to_numeric(series.astype(str).str.replace(' ', '').str.replace(',', '.', regex=False),
                                     errors='coerce')

            # Aplica a limpeza e conversão nas colunas de clima
            df['TEMP_MEDIA'] = clean_and_convert(df[col_temp_media])
            df['PRECIPITACAO'] = clean_and_convert(df[col_precip_total])
            df['PRESSAO_MEDIA'] = clean_and_convert(df[col_pressao])

            # --- 4. Cria dataframe reduzido ---
            # Mantém apenas as colunas essenciais e padroniza o nome da data
            df_reduzido = df[[col_data, 'TEMP_MEDIA', 'PRECIPITACAO', 'PRESSAO_MEDIA']].copy()

            df_reduzido['estacao'] = arq.stem.split('_')[-2]
            df_reduzido = df_reduzido.rename(columns={col_data: 'data'})

            dfs.append(df_reduzido)

        except Exception as e:
            print(f"❌ Erro ao ler {arq.name}: {e}")

    if not dfs:
        print("⚠️ Nenhum dado válido do INMET encontrado.")
        return pd.DataFrame()

    # Combina todos os DataFrames de estações em um único DF
    df_total = pd.concat(dfs, ignore_index=True)
    df_total['data'] = pd.to_datetime(df_total['data'])

    # Agrupa por data (média das estações se houver mais de uma)
    df_agg = df_total.groupby('data')[['TEMP_MEDIA', 'PRECIPITACAO', 'PRESSAO_MEDIA']].mean().reset_index()

    print(f"✅ {df_agg.shape[0]} registros mensais combinados de INMET.")
    return df_agg