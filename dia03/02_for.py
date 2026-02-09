#%%
#laço de repetição for

nome = 'Demitri'

for i in nome:
    print(i)

#numero = 1978     ** nao funciona porque nao é 
#for i in numero:     iterável
#    print(i)         int, float, bool **

lista = [1,2,3,'oi'] #indices que pode alterar
for i in lista:
    print(i)

tupla = (1,2,3,4,'oi') #valores fechados nao altera
for i in tupla:
    print(i)

dict = {'nome': 'dem', 'idade': 48, 'pais': 'es'} #chave -> valor
for i in dict:
    print(i)
for i in dict.values():
    print(i)
for i, j in dict.items():
    print(i,j)

conjunto = {'hola', 'mundo', 'oi'}
for i in conjunto:
    print(i)

contador = range(1,4)
for i in contador:
    print(i)

#%%
#tabuada
numero = 2
max_range = 10
for i in range(1, max_range+1):
    print(numero, 'x ', i, '= ', numero*i)

#numero divisivel por 4

for i in range(1, 101):
    if i % 4 == 0:
        print(i)