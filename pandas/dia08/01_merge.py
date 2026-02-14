#%%
import pandas as pd

df_tr = pd.read_csv('../data/transacoes.csv', sep=';')
df_tr.head()
#%%
df_cl = pd.read_csv('../data/clientes.csv', sep=';')
df_cl = df_cl.rename(columns={'idCliente': 'IdCliente'})
df_cl.head()
#%%
df_merge = df_tr.merge(right=df_cl,
                    how='left',
                    on=['IdCliente'],
                    suffixes=['_tr', '_cl'])
# right -> nome do dataframe da direita
# how -> left Join (mantem os valores do dataframe da esquerda)
# on -> qual é a chave estrangeira
# caso os nomes da chaves primarias e estrangeiras não batam
# usar, left_on=['IdCliente], right_on=['idCliente'], ai não precisa renomear
df_merge.head()