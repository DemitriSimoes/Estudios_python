#%%
import pandas as pd

df = pd.read_csv('../data/produtos.csv', sep=';')
df.shape
#df.notna()
#%%
df.dropna() # drop a linha toda que tenha qualquer NaN em qualquer coluna
#%%
df.dropna(how='all') # a linha inteira tem que ser NaN
#%%
df.dropna(how='all', subset=['DescDescricaoProduto']) # criterio para avaliar quais colunas que tem que ter o NaN
#%%
df.fillna('outros') # este preenche os campos que estão em NaN, este para o dataframe todo
df['DescDescricaoProduto'].fillna('sem descricao') # este para uma serie de uma coluna selecionada
#%%
# df.fillna({'nome': 'alguem', 'idade': 0}) # aqui estou lidando com dataframe,
#  então posso colocar que no nome da coluna,
#  vai um valor e em outra coluna outro valor