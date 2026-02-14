#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv')
df
#%%
df.to_csv('cliente.csv', index=False)
df
#%%
df.to_parquet('clientes.parquet', index=False)

df = pd.read_parquet('clientes.parquet')
df
#%%
df.to_excel('clientes.xlsx', index=False)

df = pd.read_excel('cliente.xlsx')
df
#%%
df = pd.read_csv('../data/ponto_virgula.csv')
print(df)
#%%
# padrao do DataFrame do pandas e separar
# por vírgula, por isso tem que por o sep
df = pd.read_csv('../data/ponto_virgula.csv', sep=';')
df