#%%
import pandas as pd

df_tr = pd.read_csv('../data/transacoes.csv', sep=';')
df_tr.head()
#%%
df_trpr = pd.read_csv('../data/transacao_produto.csv', sep=';')
df_trpr.head()
#%%
df_pr = pd.read_csv('../data/produtos.csv', sep=';')
df_pr['DescNomeProduto'][80:100]
#%%
df_merge_trpr = df_tr.merge(right=df_trpr, how='left', on='IdTransacao')
df_merge_trpr.head()
#%%
filtro = df_merge_trpr[['IdTransacao', 'IdCliente', 'IdProduto']]
filtro.head()
#%%
df_tudo = df_merge_trpr.merge(right=df_pr,
                       how='left',
                       on='IdProduto')#[['IdTransacao', 'IdCliente', 'IdProduto']]
df_tudo = df_tudo[df_tudo['DescNomeProduto'] == 'Presença Streak']
df_tudo
#%%
df_tudo.groupby(by=['IdCliente'])['IdTransacao'].count().sort_values(ascending=False).head(1)
#%%
df_pr = df_pr[df_pr['DescNomeProduto'] == 'Presença Streak']

df_merge_trpr = (df_tr.merge(right=df_trpr,
                            how='left',
                            on='IdTransacao')
                            .merge(right=df_pr,
                                   how='inner',
                                   on=['IdProduto'])
                                   .groupby('IdCliente')['IdTransacao']
                                   .count()
                                   .sort_values(ascending=False)
                                   .head(1)
)
df_merge_trpr
#%%
