#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
#%%
def novo_id(final):
    return final.split('-')[-1]

df['cliente'] = df['idCliente'].apply(novo_id) # percorre toda a seria aplicando linha a linha
df
