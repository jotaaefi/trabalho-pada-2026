import pandas as pd
from scripts.utils import *

df = pd.read_csv('../csv_original/4_pnad_educacao.csv')

            # MAPEAMENTO GERAL

df['sexo'] = cleanSpaces(df['sexo'])

df['faixa_etaria'] = cleanSpaces(df['faixa_etaria'])

df['nivel_escolaridade'] = cleanSpaces(df['nivel_escolaridade'])

save_csv(df,'4_pnad_educacao_FINAL.csv' )



#3. Base da PNAD Educação (4_pnad_educacao.csv)
   # [x ] Limpeza de Strings (Strip): Tratar as colunas de texto geradas pelo CASE WHEN do SQL (sexo, faixa_etaria, nivel_escolaridade).

   # [ x ] Verificação de Consistência: Garantir que os nomes do nível de escolaridade batam ortograficamente com os que serão criados na RAIS.

   # [ x ] Exportação Final: Salvar como 4_pnad_educacao_FINAL.csv.