# Selecione a primeira transacao diaria de
# cada cliente
#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')

df.head()
#%%
df['DtCriacao'] = pd.to_datetime(df['DtCriacao'])
#%%
df.head()
df = df.sort_values('DtCriacao', ascending=False)
df['data'] = df['DtCriacao'].dt.date
df.head()
#%%
df = df.drop_duplicates(subset=['IdCliente', 'data'])
df.head()