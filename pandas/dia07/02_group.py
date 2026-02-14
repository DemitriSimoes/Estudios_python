#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()
#%%
df.groupby(by=['IdCliente'], as_index=False).sum('QtdePontos')
df.groupby(by=['IdCliente']).count()
# as_index=False -> deixa o indice do dataframe
# ou 
# df.groupby(by=['IdCliente'])['QtdePontos'].sum()
# retorna uma serie
# df.groupby(by=['IdCliente'])[['QtdePontos']].sum()
# retorna um dataframe
#%%
# qtd de transacoes
# qtd e pontos
# media de pontos
# usa-se 'agg' -> agregação
summary = df.groupby(by=['IdCliente']).agg({
    'IdTransacao': ['count'],
    'QtdePontos': ['sum', 'mean']
})
#%%
summary[('QtdePontos', 'mean')]
#%%
summary.columns = ['IdTransacao', 'Somaqtpontos', 'mediaqtpontos']
summary