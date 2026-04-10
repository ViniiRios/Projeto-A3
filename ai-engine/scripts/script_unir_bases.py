import pandas as pd


def unir_bases_sinan_inmet(df_sinan, df_inmet):
    """
    Junta os dados do SINAN (já agregado mensalmente por agravo) e INMET pela data.
    """
    # Agrupa o total de casos de TODOS os agravos por mês para o merge com o INMET
    df_sinan_agg_dia = df_sinan.groupby('data')['casos'].sum().reset_index(name='casos_total_mes')

    # Faz o merge usando a coluna 'data' padronizada em ambos os DFs
    df_final = pd.merge(df_inmet, df_sinan_agg_dia, on='data', how='left')

    # Preenche meses sem notificação de casos com zero
    df_final['casos_total_mes'] = df_final['casos_total_mes'].fillna(0)

    return df_final