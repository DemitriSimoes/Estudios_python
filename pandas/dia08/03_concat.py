#%%
import pandas as pd

df = pd.DataFrame({
    'cliente': [1,2,3,4,5],
    'nome': ['De', 'Si', 'Ca', 'He', 'Nan'],
})
df02 = pd.DataFrame({
    'cliente': [6,7,8],
    'nome': ['Mi', 'Mo', 'Des'],
    'idade': [48,49,50]
})
df03 = pd.DataFrame({
    'idade': [48,49,47,50,51]
})
#%%
# concat empilha os dataframe, diferente do merge que mescla colocando um dataframe do lado de outro
# concat espera uma lista
dfs = [df, df02]

pd.concat(dfs, ignore_index=True)
#%%
df03 = df03.sort_values('idade').reset_index(drop=True)
df03
#%%
pd.concat([df, df03], axis=1)
