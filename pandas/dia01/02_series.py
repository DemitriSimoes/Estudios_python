#%%

edades_list = [
    25, 35, 45,
    55, 23, 34,
    46, 48, 31
]

import pandas as pd

series_edad = pd.Series(edades_list)
print(series_edad)
type(series_edad)
#%%
media = series_edad.mean()
print(media)
variancia = series_edad.var()
print(variancia)
print(variancia **0.5)#desvio padrao = std
dados_estat = series_edad.describe()
print(dados_estat)