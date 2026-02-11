#%%
import pandas as pd
#%%
teste = pd.DataFrame(
    {
        'Nombres': ['De', 'Si', 'Ca', 'He'],
        'Edades': ['48', '49', '17', '15'],
        'Comu': ['Gali', 'Madr', 'Bilb', 'Valla']
    }
)
#%%
result = teste['Edades'].astype(int) >= 18
type(result)
result
teste[result]
# teste[teste['Edades'].astype(int)>=18]
#%%
df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()
#%%
df_50 = df['QtdePontos'] >=50
df[df_50].shape # mostra quantidade de linhas e colunas (uma tupla com dois valores)
#%%
df[df_50].dtypes # mostra o tipo de dado de cada coluna
df[df_50]
#%%
df_50_100 = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100)
df[df_50_100]
#%%
df_1_100 = (df['QtdePontos'] == 1) | (df['QtdePontos'] > 100)
df[df_1_100]