import pandas as pd
from pathlib import Path

# Constantes para o processamento
MESES = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
# Define o código de busca para Belo Horizonte
COD_BELO_HORIZONTE_BUSCA = 3106207
COD_BELO_HORIZONTE_FINAL = 3106207


def get_dados_sinan_local(pasta="dados/dados_brutos", municipio_id=COD_BELO_HORIZONTE_BUSCA):
    """
    Lê e combina os 6 arquivos SINAN minimalistas, usando o código de 7 dígitos.
    (Corrigido o problema de formatação de data com zero-padding).
    """
    # Procura por arquivos que terminam em _bh_minimal.csv
    arquivos = list(Path(pasta).glob("sinan_*.csv"))
    if not arquivos:
        print(
            "⚠️ Nenhum arquivo SINAN minimalista encontrado. Crie os 6 arquivos e renomeie-os como *__bh_minimal.csv.")
        return pd.DataFrame()

    dfs = [] # Lista para armazenar as séries temporais de cada arquivo

    for arq in arquivos:
        print(f"📥 Lendo e processando {arq.name} (Minimalista) ...")

        try:
            # --- 1. Leitura do CSV: Usa separador ';', quotechar='"' e encoding 'latin1' (padrão DATASUS) ---
            df = pd.read_csv(arq, sep=';', encoding='latin1', low_memory=False, quotechar='"')

            # --- 2. Renomear Coluna: Assume que a primeira coluna é o código/nome do município ---
            coluna_municipio_real = df.columns[0]
            df.rename(columns={coluna_municipio_real: 'CODIGO_NOME_MUNICIPIO'}, inplace=True)

            # --- 3. Extração e Filtro: Isole a linha de Belo Horizonte (BH) ---
            # Extrai o código IBGE (o primeiro bloco de dígitos)
            df['CODIGO_MUNICIPIO'] = df['CODIGO_NOME_MUNICIPIO'].astype(str).str.split(' ').str[0]
            df['CODIGO_MUNICIPIO'] = pd.to_numeric(df['CODIGO_MUNICIPIO'], errors='coerce').fillna(-1).astype(int)

            # Filtra a linha de BH (no caso do arquivo minimalista, é a única linha)
            df = df[df['CODIGO_MUNICIPIO'] == municipio_id].copy()

            if df.empty:
                print(f"⚠️ {arq.name} ignorado: Linha de BH ({municipio_id}) não encontrada no arquivo minimalista.")
                continue

            # --- 4. Extrair Ano e Agravo ---
            # Extrai o tipo de agravo (dengue, zika, chikungunya) e o ano do nome do arquivo
            nome_base = arq.stem
            agravo = nome_base.split('_')[1].upper()
            ano = int(nome_base.split('_')[2])

            # --- 5. Limpeza das Colunas de Casos ---
            # Remove caracteres não-numéricos (Ex: '-') e converte os casos para inteiro
            for col in MESES:
                if col in df.columns:
                    df[col] = df[col].astype(str).str.replace(r'[^0-9]', '', regex=True)
                    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
                else:
                    df[col] = 0

            # --- 6. UN-PIVOT (MELT): Transforma colunas Jan-Dez em linhas ---
            # Cria a série temporal: cada mês vira uma linha com sua contagem de casos
            df_melt = df.melt(
                value_vars=MESES,
                var_name='mes',
                value_name='casos'
            )

            # --- 7. Criar a Coluna de Data/Mês CORRETA (Correção de Zero-Padding) ---
            # Combina Ano e Mês para criar a data (YYYY-MM-DD)
            df_melt['ano'] = ano
            mes_map = {m: i + 1 for i, m in enumerate(MESES)}
            df_melt['mes_num'] = df_melt['mes'].map(mes_map)

            # Garante que o mês tenha dois dígitos (Ex: 01)
            df_melt['mes_num_str'] = df_melt['mes_num'].astype(str).str.zfill(2)

            # Converte a string final para o formato datetime
            df_melt['data'] = pd.to_datetime(
                df_melt['ano'].astype(str) + '-' + df_melt['mes_num_str'] + '-01',
                format='%y-%m-%d' # Usa %y (2 dígitos) para o ano
            )

            df_melt['agravo'] = agravo

            # Adiciona a série temporal limpa à lista de DataFrames
            dfs.append(df_melt[['data', 'agravo', 'casos']].dropna(subset=['data']))

        except Exception as e:
            print(f"❌ Erro ao ler {arq.name}: {e}")

    if not dfs:
        print("⚠️ Nenhum dado válido do SINAN encontrado.")
        return pd.DataFrame()

    # --- 8. Combina e Agrupa ---
    # Concatena todas as séries (Dengue, Zika, Chikungunya) e agrega
    df_total = pd.concat(dfs, ignore_index=True)
    df_agg = df_total.groupby(['data', 'agravo'])['casos'].sum().reset_index()

    print(f"✅ {df_agg['casos'].sum()} casos mensais combinados de {len(arquivos)} arquivos SINAN.")
    return df_agg