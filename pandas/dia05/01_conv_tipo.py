#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
#%%
# conversao de tipo
df['qtdePontos'].astype(float)
#%%
zero = df['DtCriacao'][::] == '0000-00-00 00:00:00.000'
df[zero]
# caso tenha dado erro em alguma data tem
# que usar REPLACE
# df['DtCriacao'].replace(
#               {'0000-00-00 00:00:00.000':
#               '2020-01-01 07:00:00.000'})
#%%
df['DtCriacao'] = pd.to_datetime(df['DtCriacao'])
df['DtCriacao'].dt.date