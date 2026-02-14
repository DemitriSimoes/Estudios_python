#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
#%%
df['soma_100'] = df['qtdePontos'] +100
df
#%%
# nova_coluna = []
# for i in df['qtdePontos']:
#     nova_coluna.append(i+100)

# nova_coluna
#%%
df['emailTwitch'] = df['flEmail'] + df['flTwitch']
df
#%%
import numpy as np

df['logpontos'] = np.log(df['qtdePontos']+1)
df['logpontos'].describe()
#%%
