import pandas as pd

from scripts.utils import *

# 1. Dicionário padronizado no formato oficial do IBGE para os gráficos do Power BI
MAP_RACA_COR = {
        1: "Branca",
        2: "Preta",

        # Tratamento para as variações de Parda
        3: "Parda",
        8: "Parda",

        # Tratamento para as variações de Amarela
        4: "Amarela",
        5: "Amarela",

        # Indígena e Não informado
        6: "Indígena",
        9: "Não informado"
    }

MAP_FORCA_TRABALHO = {

        1: "Na força de trabalho", # (Pessoas ocupadas ou desocupadas que estão na busca)
        2: "Fora da força de trabalho" # (Pessoas inativas economicamente)
}

df = pd.read_csv('../csv_original/3_pnad_mercado.csv')

print("Aplicando o tratamento de dados nas colunas...")

df['raca_cor'] = mappingValues(df['raca_cor'], MAP_RACA_COR)

#df['condicao_forca_trabalho'] = fillNaNs(df['condicao_forca_trabalho'], 0)
df['condicao_forca_trabalho'] = mappingValues(df['condicao_forca_trabalho'], MAP_FORCA_TRABALHO)
df['condicao_forca_trabalho'] = df['condicao_forca_trabalho'].fillna('Na força de trabalho').astype(str).str.strip()

df = df.drop(df[df['sigla_uf'] == 'IGNORADO'].index)

df['sexo'] = cleanSpaces(df['sexo'])
df['sigla_uf'] = cleanSpaces(df['sigla_uf'])
df['categoria_ocupacao'] = cleanSpaces(df['categoria_ocupacao'])


df['rendimento_medio_trabalho'] = toNumeric(df['rendimento_medio_trabalho'])
df['rendimento_medio_trabalho'] = fillNaNs(df['rendimento_medio_trabalho'], 0)
df['rendimento_medio_trabalho'] = df['rendimento_medio_trabalho'].round(2)


save_csv(df, "3_pnad_mercado_FINAL.csv")

    #Base da PNAD Mercado (3_pnad_mercado.csv)
    #[x] Padronização de Raça/Cor: Mapeamento numérico convertido para texto limpo (corrigindo e incluindo os códigos legados 3 e 5 capturados no terminal).

    #[ x  ] Limpeza de Strings (Strip): Aplicar a remoção de espaços em branco nas colunas de texto (sexo, sigla_uf, categoria_ocupacao).

    # [ x ] Tratamento de Nulos: Verificar se a coluna rendimento_medio_trabalho gerou algum valor nulo ou vazio e forçar para 0 ou tratar médias vazias.

    # [ ] Exportação Final: Salvar como 3_pnad_mercado_FINAL.csv.







