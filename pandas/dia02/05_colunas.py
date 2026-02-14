#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')

df.head()
#%%
df.shape
#%%
df.info(memory_usage='deep')
#%%
df.dtypes
#%%
# renomeando
colunas = {'QtdePontos': 'QtPontos',
                   'DescSistemaOrigem': 'SistOrigem'
                   }
#df = df.rename(columns={'QtdePontos': 'QtPontos',
#                   'DescSistemaOrigem': 'SistOrigem'
#                   })

df.rename(columns=colunas, inplace=True)
df.head()
#%%
df['IdCliente'].head() # retorna uma serie
#%%
# df[['IdCliente', 'QtPontos']].head() # retorna um dataframe
colun = ['IdCliente', 'QtPontos']
df[colun].head()
#%%
# SELECT * FROM df
df
#%%
# SELECT Idcliente FROM df
df[['IdCliente']]
# SELECT IdCliente, QtPontos FROM df LIMIT 5
df[['IdCliente', 'QtPontos']].tail(5)
#%%
# reordenando colunas
nova_ordem = list(df.columns) # cria uma lista
nova_ordem.sort() # ordena a lista
nova_ordem
#%%
df = df[nova_ordem] # atribui a ordem da lista
df.head()