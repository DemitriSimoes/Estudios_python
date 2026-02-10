#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head() # mostra as 5 primeiras linhas 
#%%
df.tail()
#%%
df.sample(5)
#%%
df.shape # .shape é um atributoo e não um método, retorna uma tupla, qtd de linha e qtd de colunas
#%%
df.columns # retorna o nome das colunas
#%%
df.index # retorna o index do dataframe
#%%
df.info(memory_usage='deep')
#%%
df.dtypes # um atributo que mostra uma seria da tipagem de cada campo
