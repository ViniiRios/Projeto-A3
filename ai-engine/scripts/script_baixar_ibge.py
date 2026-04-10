import pandas as pd

# Mude o caminho CSV para o novo arquivo minimalista
def get_populacao_local(codigo_municipio, caminho_csv="dados/dados_brutos/populacao_ibge_25.csv"):
    """
    Lê a população estimada de Belo Horizonte a partir de um arquivo CSV minimalista
    criado manualmente.
    """
    try:
        # Leitura da tabela minimalista (sem skiprows, usando UTF-8)
        # Assume que o arquivo minimalista tem o formato mais limpo possível
        df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8')

        # Colunas fixas neste arquivo minimalista
        col_codigo = 'CODIGO_MUNICIPIO'
        col_pop = 'POPULACAO_ESTIMADA'
        col_nome = 'NOME_MUNICIPIO'

        # --- 1. O código já está na primeira e única linha ---
        # Captura a primeira linha, que deve ser a de Belo Horizonte
        linha = df.head(1)

        if not linha.empty:
            # --- 2. Extrair a população e limpar possíveis formatações (ponto/vírgula) ---
            # Converte o valor de população para string e remove o separador de milhar
            pop_bruta = linha[col_pop].values[0]
            pop = int(str(pop_bruta).replace('.', '').replace(',', ''))

            nome_municipio = linha[col_nome].values[0]

            print(f"✅ Sucesso! População de {nome_municipio} ({codigo_municipio}): {pop}")
            return pop
        else:
            print(f"⚠️ Município {codigo_municipio} não encontrado. O arquivo minimalista está vazio.")
            return None

    except Exception as e:
        # Captura e exibe qualquer erro de leitura ou conversão
        print("❌ Erro ao ler o CSV do IBGE:", e)
        return None