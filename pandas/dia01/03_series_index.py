#%%

edades_list = [
    25, 35, 45,
    55, 23, 34,
    46, 48, 31
]

import pandas as pd

series_edad = pd.Series(edades_list)
print(series_edad)
#%%
print(edades_list[0])
print(series_edad[0])

print(edades_list[-1])
# print(series_edad[-1]) # não funciona, pois as chaves das serias funciona como as chaves de dicionario, não é pelo nome e sim pelo seu número
#%%
for i, j in series_edad.items():
    print('Indice: ', i, '-> valor: ', j)

print(series_edad[series_edad.index[-1]])
#%%
series_edad = series_edad.sort_values()

print(series_edad)
# iloc funciona como uma lista, ai sim pode usar os números 0, -1 etc
print(series_edad.iloc[0]) 
print(series_edad.iloc[-1])
#%%
edades_list = [
    25, 35, 45,
    55, 23, 34,
    46, 48, 31
]

indexs = [
    'De', 'Si', 'Ca',
    'He', 'Mi', 'Mo',
    'Lo', 'Nan', 'Des'
]

series_idx = pd.Series(edades_list, index=indexs)
print(series_idx)

print(series_idx['Mo'])
print(series_idx.iloc[-1])
print(series_idx.iloc[::-2])