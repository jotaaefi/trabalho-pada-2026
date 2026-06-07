import pandas as pd

from scripts.utils import cleanSpaces, toNumeric, save_csv

df = pd.read_csv('../csv_original/5_pnad_rendimentos.csv')

df['sexo'] = cleanSpaces(df['sexo'])
df['faixa_etaria'] = cleanSpaces(df['faixa_etaria'])


        #MAPEAMENTO DA MEDIA DOS SALARIOS

    # 1. Força a conversão para número (o que for texto de erro vira NaN e depois 0)
df['media_aposentadoria_pensao'] = toNumeric(df['media_aposentadoria_pensao'])
df['media_pensao_alimenticia'] = toNumeric(df['media_pensao_alimenticia'])
df['media_programas_sociais'] = toNumeric(df['media_programas_sociais'])
df['media_outros_rendimentos'] = toNumeric(df['media_outros_rendimentos'])

    # 2. Arredonda todas elas para 2 casas decimais
df['media_aposentadoria_pensao'] = df['media_aposentadoria_pensao'].round(2)
df['media_pensao_alimenticia'] = df['media_pensao_alimenticia'].round(2)
df['media_programas_sociais'] = df['media_programas_sociais'].round(2)
df['media_outros_rendimentos'] = df['media_outros_rendimentos'].round(2)


save_csv(df, '5_pnad_rendimentos_FINAL.csv')




#4. Base da PNAD Outros Rendimentos (5_pnad_rendimentos.csv)
# [ x] Limpeza de Strings (Strip): Tratar as colunas de texto (sexo, faixa_etaria).

# [ ] Arredondamento e Consistência Financeira: Garantir que todas as médias monetárias estejam com duas casas decimais e sem valores textuais de erro.

# [ ] Exportação Final: Salvar como 5_pnad_rendimentos_FINAL.csv.