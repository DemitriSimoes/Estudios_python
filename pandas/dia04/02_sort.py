#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
#%%
df.sort_values(by='qtdePontos', ascending=False).head()
# ordenando o dataframe
#%%
(df.sort_values(by='qtdePontos', ascending=False)
 .head(5)['idCliente']) # usa o parentes para usar quebra de linha
#%%
# caso tenha EMPATE na qtdePontos eu posso
# passar uma lista com mais colunas para filtrar
(df.sort_values(by=['qtdePontos', 'DtCriacao'], ascending=False)
 .head(5))
#%%
# isso pode ser feito pelo ASCENDING  tambem
# colocar uma lista e filtrar com True e False
(df.sort_values(by=['qtdePontos', 'DtCriacao'], ascending=[False, True])
 .head(5))