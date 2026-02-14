#%%
import pandas as pd
edades = [
    25, 35, 45,
    55, 23, 34,
    46, 48, 31
]

nombres = [
    'De', 'Si', 'Ca',
    'He', 'Mi', 'Mo',
    'Lo', 'Nan', 'Des'
]

s_edad = pd.Series(edades)
s_nombre = pd.Series(nombres)
print(s_edad)
print(s_nombre)
#%%
# é como um varal onde vou pendurando as coisas, 
# dou nome ao varal, que são as colunas e penduro
# por exemplo, uma serie

df_varal = pd.DataFrame()
print(df_varal)
df_varal['Edades'] = s_edad
print(df_varal)
df_varal['Nombres'] = s_nombre
print(df_varal)

#%%
# o DataFrame tem uma lista dentro dele,
# como se fosse um dicionario de chave
# e nos valores tem listas dentro,
# mais especificamente listas de listas
# e que é uma série
print(df_varal['Edades'])
print(df_varal.iloc[0])
# se eu pegar o iloc de uma série,
# eu pego a linha em relação ao
# índice linha
# se eu pegar o iloc de um DataFrame,
# eu pego as linhas de uma coluna,
# onde ele retorna uma serie a qual
# o indice eh o nome da coluna e o
# valor a linha de indice 0 por exemplo
print(df_varal.iloc[-1]['Edades'])
#%%
print(df_varal['Edades'].describe())