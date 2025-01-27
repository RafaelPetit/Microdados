'''
Este programa extraira uma amostra aleatoria de dados do ENEM 2023
'''

import pandas as pd

NUM_MAX_LINHAS = 100000

# Carrega o arquivo de dados do ENEM
df = pd.read_csv('MICRODADOS_ENEM_2023.csv', sep=';', encoding='latin1')

# Criar uma amostra aleatoria de NUM_MAX_LINHAS de dados do ENEM 2022
df_amostra = df.sample(n=NUM_MAX_LINHAS)

# Salva a amostra em um arquivo CSV
df_amostra.to_csv('amostra_enem_2023_100k.csv', sep=';', index=False)