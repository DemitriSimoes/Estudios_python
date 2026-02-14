#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
#%%
df_stack = (df.set_index(
    ['idCliente',
     'qtdePontos',
     'DtCriacao',
     'DtAtualizacao'])
     .stack()
     .reset_index())
df_stack.columns = ['idCliente','qtdePontos','DtCriacao','DtAtualizacao','redes_soc', 's/n']
df_stack.head()
#%%
df_stack.pivot_table(values='s/n',
                     index=['idCliente',
                            'qtdePontos',
                            'DtCriacao',
                            'DtAtualizacao'],
                    columns='redes_soc').reset_index()
#%%
df_stack.pivot_table(values='s/n',
                     index=['idCliente',
                            'DtCriacao',
                            'DtAtualizacao'],
                    columns='redes_soc',
                    aggfunc='sum')
