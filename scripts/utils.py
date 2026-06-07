import os
import sys
import pandas as pd

def cleanSpaces(value):
    return value.str.strip()

def mappingValues(key, mapping_values, ):
    # Key: Value
    return key.map(mapping_values)

def toNumeric(df):
    return pd.to_numeric(df, errors='coerce')

def fillNaNs(column, values):
        return column.fillna(values)


def round_values(value):
    return round(value)

def save_csv(dataframe, nome_arquivo):
    pasta_atual = os.path.abspath(os.getcwd())

    # 2. Garante que estamos a apontar para a pasta do trabalho principal
    if "scripts" in pasta_atual.lower():
        raiz = os.path.dirname(pasta_atual)
    else:
        raiz = pasta_atual

    caminho_final = os.path.join(raiz, "csv_limpo", nome_arquivo)

    # 3. Cria a pasta se ela não existir por algum motivo
    os.makedirs(os.path.dirname(caminho_final), exist_ok=True)

    # 4. Salva o arquivo
    dataframe.to_csv(caminho_final, index=False)

    # 5. O truque do flush=True + sys.stdout.flush() para forçar o PyCharm a imprimir
    print(f"\n>>> [OK] ARQUIVO SALVO EM: {caminho_final}", flush=True)
    sys.stdout.flush()
