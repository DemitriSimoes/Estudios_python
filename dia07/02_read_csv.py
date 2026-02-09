#%%
archivo = 'data.csv'

with open(archivo) as open_file:
    data = open_file.readlines()

for i in data:
    print(i)
#%%
len(data)
chaves = data[0].strip('\n').split(';')
dict_novo = dict()
for i in chaves:
    dict_novo[i] = []

for linea in data[1:]:
    valores = linea.strip('\n').split(';')
    #for i in range(len(valores)):
       # dict_novo[chaves[i]].append(valores[i])
    for chave, valor in zip(chaves, valores):
        dict_novo[chave].append(valor)
dict_novo
#%%
idade = []
for i in dict_novo['idade']:
    idade.append(int(i))
print(idade)
from statistics import mean
print(mean(idade))
media = sum(idade)/ len(idade)
print(media)
#%%
for i, j in zip(dict_novo['idade'],
                 range(len(dict_novo['idade']))):
    dict_novo['idade'][j] = int(i)

# dict_novo['idade'] = [int(i) for i in dict_novo['idade']]
# jeito mais limpo e correto de fazer mudança da coluna
# enumerate já pega o index (idx) direto sem 
# precisar fazer range(len(dict_novo['idade']))
# ficaria assim: for i, j in enumerate(dict_novo['idade'])
# dict_novo['idade'][i] = int(j)
dict_novo