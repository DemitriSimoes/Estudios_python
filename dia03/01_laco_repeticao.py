#%%
#laço de repetição
tabuada = int(
    input(
        'Entre com um valor' \
        ' inteiro para calcular sua tabuada: '))
count = 1

while count <= 10:
    print('Valor de ', count, ' x',  tabuada, '= ', count*tabuada)
    count += 1 # count = count + 1

#%%
#divisivel por 4

numero = 4

while numero <= 100:
    if numero % 4 == 0:
        #resultado = numero // 4
        print(numero, '-> divisivel por 4')#, '/ 4', '= ', resultado)
        
    numero += 1
print('fim')

#%%
#soma das alturas
altura_soma = 0 #valor de entrada
entrada = 4 #contador

while entrada > 0:
    alturas = input('Entre com uma altura: ')
    alturas = float(alturas)
    altura_soma += alturas
    entrada -= 1
print('Soma das alturas: ', altura_soma)
#%%
#soma das alturas usando for
altura_soma=0
entrada=4
for i in range(entrada):
    alturas = input('Entre com uma altura: ')
    alturas = float(alturas)
    altura_soma+=alturas
print('A soma das alturas: ', altura_soma)
#%%
#saldo total
saldo_total = 0

while True:
    valor = input('Entre com um valor: ')
    if valor == '':
        break #serve para parar o laço mais proximo
    saldo_total+=float(valor)

print('Valor total = $', saldo_total)