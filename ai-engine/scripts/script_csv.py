import os
import pandas as pd


def salvar_csv(df, nome_arquivo, pasta='dados/tratados'):
    """Salva DataFrame em CSV na pasta especificada."""
    os.makedirs(pasta, exist_ok=True)
    caminho = f"{pasta}/{nome_arquivo}.csv"

    # Usando o separador ';' para garantir a leitura correta em outras ferramentas
    df.to_csv(caminho, index=False, encoding='utf-8', sep=';')
    print(f"✅ Arquivo salvo em: {caminho}")