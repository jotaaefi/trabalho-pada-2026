import pandas as pd

from scripts.utils import *



df = pd.read_csv('../csv_original/1_rais_historico_1985_2025.csv')

df['sexo'] = cleanSpaces(df['sexo'])
df['sigla_uf'] = cleanSpaces(df['sigla_uf'])

df = df.drop(df[df['sigla_uf'] == 'IGNORADO'].index)

df['salario_medio'] = toNumeric(df['salario_medio'])
df['salario_medio'] = fillNaNs(df['salario_medio'], 0)
df['salario_medio'] = df['salario_medio'].round(2)

save_csv(df, "1_rais_historico_FINAL.csv")


    #5. Base da RAIS Histórico (1_rais_historico_1985_2025.csv)
    #[ x ] Limpeza de Strings (Strip): Garantir que a coluna sexo e sigla_uf não tenham espaços antes ou depois.

    #[ ] Exportação Final: Salvar como 1_rais_historico_FINAL.csv.

    #Qual é o próximo item do checklist que você quer atacar agora no PyCharm? Se quiser, podemos fazer o tratamento da Escolaridade da RAIS ou a remoção das linhas 'IGNORADO' da UF. É só mandar!