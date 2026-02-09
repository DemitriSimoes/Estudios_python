#%%
lista_pessoa = ['nome', 48, 'end', 'pais', True]

print(lista_pessoa)

print(lista_pessoa[1])
print(lista_pessoa[4])

#%%
lista_numeros = [50,50,62,49,46,71,26,35,46,52]

print('soma: ', sum(lista_numeros))
print('Tamanho: ', len(lista_numeros))
print('Media: ', sum(lista_numeros) / len(lista_numeros))
print('Maximo: ', max(lista_numeros))
print('Minimo: ', min(lista_numeros))

#%%
pessoa = ['nome',
        48,
        'local', 
        ['estag', 'junior', 'pleno', 'senior'],
        ['manzana', 'uva', 'limon']]

print(pessoa[2])
print(pessoa[len(pessoa)-1])
print(pessoa[-1])
print(pessoa[-1][0])
print(pessoa[-1][-2])

#%%
print(pessoa[0:3]) #pega pelos indices, mas nao pega o ultimo
print(pessoa[-2][-2:])
#pessoa[start: stop] -> se ocultar um deles vai considerar 0 para start e até o final para stop
#pessoa[start:stop:step] -> step quer dizer de quanto quer navegar, se colocar -1 ou -2 vai de trás para frente

print(pessoa[-2][::-1])

#%%
#quantas vezes o numero aparece

lista = [2,2,3,5,6,1,4,1,8,9,8,7,9,8,6,3,2,1,0,4]

numero = input('Escolha um numero de 0 a 9: ')
numero = int(numero)

contador = 0
for i in lista:
    if i == numero:
        contador+=1
print('Quantidade de ', numero, '= ', contador)

#%%
#idades

idades =[]

while True:
    idade = input('Digite sua idade: ')
    if idade == '':
        break
    idades.append(int(idade))

print(idades)
media = sum(idades)/len(idades)
maximo = max(idades)
minimo = min(idades)
soma = sum(idades)

print('MEDIA: ', media)
print('MAXIMO: ', maximo)
print('MINIMO: ', minimo)
print('SOMA: ', soma)
