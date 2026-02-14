#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()
#%%
from numpy import sqrt
def ampli_media(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return sqrt((amplitude - media)**2)

serie = pd.Series([46,48,43,48,26,35,65,85,15,68])

ampli_media(serie)
#%%

summary = df.groupby(by=['IdCliente']).agg({
    'IdTransacao': ['count'],
    'QtdePontos': ['sum', 'mean', ampli_media]
})
summary