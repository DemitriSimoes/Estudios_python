#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
#%%
filtro = df['qtdePontos'] == 0
# clientes_0 = df[filtro] # pandas cria um view
# filtro = df.loc[df['qtdePontos] == 0, 'flag_1] = 1 # aqui altera o original
clientes_0 = df[filtro].copy() # cria uma copia
clientes_0['flag_1'] = 1

clientes_0