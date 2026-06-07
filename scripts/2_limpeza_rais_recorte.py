import pandas as pd
from utils import *

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

MAP_ESCOLARIDADE = {
        1: "Até Fundamental Incompleto",  # Analfabeto
        2: "Até Fundamental Incompleto",  # Até 5ª série incompleta
        3: "Fundamental Incompleto",      # 5ª série completa
        4: "Fundamental Incompleto",      # Fundamental incompleto (6ª a 9ª)
        5: "Fundamental Completo",        # Fundamental completo
        6: "Médio Incompleto",            # Médio incompleto
        7: "Médio Completo",              # Médio completo
        8: "Superior Incompleto",         # Superior incompleto
        9: "Superior Completo",           # Superior completo
        10: "Pós-Graduação",              # Mestrado
        11: "Pós-Graduação",              # Doutorado
        -1: "Sem instrução / Não informado" # Ignorado/Não informado na RAIS
    }


    # 2. Lendo o arquivo original
df = pd.read_csv('../csv_original/2_rais_recorte_2012_2025.csv')

            # MAPEAMENTO GERAL
df['raca_cor'] = mappingValues(df['raca_cor'], MAP_RACA_COR)

df = df.drop(df[df['sigla_uf'] == 'IGNORADO'].index)

df['sexo'] = cleanSpaces(df['sexo'])

            # MAPEAMENTO DA ESCOLARIDADE
df['escolaridade'] = mappingValues(df['escolaridade'], MAP_ESCOLARIDADE)

df['escolaridade'] = fillNaNs(df['escolaridade'], "String / Sem instrução / Não informado")

df['cbo_grande_grupo'] = fillNaNs(df['cbo_grande_grupo'], 0)
df['cbo_grande_grupo'] = df['cbo_grande_grupo'].astype(int)

df['salario_medio'] = fillNaNs(df['salario_medio'], 0)
df['salario_medio'] = df['salario_medio'].round(2)

            # IMPORT FINAL
save_csv(df, "2_rais_recorte_FINAL.csv" )




    #1. Base da RAIS Recorte (2_rais_recorte_2012_2025.csv)
    #[x] Padronização de Raça/Cor: Mapeamento numérico convertido para texto institucional do IBGE (Branca, Preta, Parda, Amarela, Indígena, Não informado).

    #[ x ] Filtro de Ruído Geográfico: Remover as linhas onde a coluna sigla_uf veio preenchida como 'IGNORADO' para proteger os visuais de mapa no Power BI.

    #[X ] Mapeamento de Escolaridade: Traduzir os códigos numéricos da RAIS (1 a 11) para grandes blocos de texto que coincidam exatamente com as categorias que geramos na PNAD Educação.

    #[x] Limpeza de Strings (Strip): Aplicar a remoção de espaços em branco invisíveis nas colunas de texto (sexo e sigla_uf).

    #[ ] Exportação Final: Salvar como 2_rais_recorte_FINAL.csv.

















