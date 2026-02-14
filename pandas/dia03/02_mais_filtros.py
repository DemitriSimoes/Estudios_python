#%%
import pandas as pd

df = pd.read_csv('../data/transacao_produto.csv', sep=';')
df.shape # qtd de linhas e colunas
# df.dtypes # tipos de dados de cada coluna

#%%
produto_5_11 = (df['IdProduto'] == '5') | (df['IdProduto'] == '11')
# type(df['IdProduto'][0])
df[produto_5_11].head()
#%%
produto_511 = df['IdProduto'].isin([5,11])
df[produto_511].head()
#%%
df_client = pd.read_csv('../data/clientes.csv', sep=';')
df_client.head()
df_client.info()
df_client.isna().sum() # ou df_client.isnull().sum()
#%%
dtcriacao = df_client['DtCriacao'].isna()
# df_client['DtCriacao'].notna() # negação de nulo
# ~df_client['DtCriacao'].isna() # também é uma negação usando o '~'
#listdf = list(df_client.columns)
df_client[dtcriacao]
