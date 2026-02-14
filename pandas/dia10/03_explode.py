#%%
import pandas as pd

df = pd.DataFrame({
    'idCliente':[1,2,1,2,3,4,3,1,2,3,1,1],
    'dtTransacao':['2025-01-01',
                   '2025-01-26',
                   '2025-02-19',
                   '2025-01-29',
                   '2025-01-14',
                   '2025-01-16',
                   '2025-01-22',
                   '2025-01-30',
                   '2025-02-04',
                   '2025-03-03',
                   '2025-02-22',
                   '2025-03-17'],
    'vlVenda':[3243,423,123,543,123,65,435,234,1237,543,9723,1368],
    'qtParcelas':[4,2,1,2,2,1,3,1,5,5,7,2]
})
df
#%%
df['dtTransacao'] = pd.to_datetime(df['dtTransacao'])
df
#%%
df['vlParcelas'] = df['vlVenda'] / df['qtParcelas']
df['ordemParcela'] = df.apply(lambda row: [i for i in range(row['qtParcelas'])], axis=1)
df_explode = df.explode('ordemParcela')
#%%
df_explode
#%%
def calcDtparcela(row):
    dt = row['dtTransacao']+pd.DateOffset(months=row['ordemParcela'])
    dt = f'{dt.year}-{dt.month}'
    return dt
df_explode['dtParcela'] = df_explode.apply(calcDtparcela, axis=1)

(df_explode.groupby(['idCliente', 'dtParcela'])
                    ['vlParcelas'].sum()
                    .reset_index()
                    .pivot_table(index='idCliente',
                                 columns='dtParcela',
                                 values='vlParcelas',
                                 fill_value=0))
