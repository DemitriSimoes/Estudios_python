#%%
#funcoes
print('Hola mundo')
#%%
#criando uma função
def f(x):
    resultado = 1 + x
    return resultado

f(1)

def g():
    nome = input('Escreva seu nome: ')
    print('Hola ', nome)

g()
#%%
def juros_compostos(aporte:int, taxa:float, anos:int):
    ''' Juros compostos, para calcular o retorno
    do montante aplicado por uma taxa em 
    determinada quantidade de anos
    aporte:
            valor a ser aplicado
    taxa:
            taxa de juros
    anos:
            quantidade de anos
    '''
    calculo = aporte * (1+taxa) ** anos
    return calculo

ap = float(input('Entre com aporte inicial: '))
tx = float(input('Ente com a taxa: '))
an = float(input('Entre com os anos de investimento: '))

juros_compostos(aporte=ap, taxa=tx, anos=an)
#%%
def par_impar(x:int):
    resultado = x % 2
    if resultado == 0:
        print(x, 'é par')
    else:
        print(x, 'é impar')

num = int(input('Entre com um número inteiro: '))

par_impar(num)
#%%
#estadistica
def soma(valores:list)->float:
    return sum(valores)

def media(medias:list)->float:
    return soma(medias) / len(medias)

a = float(input('Entre com um valor: '))
b = float(input('Entre com um valor: '))
c = float(input('Entre com um valor: '))

print('Media: ', media([a, b, c]))
#%%
#args
def soma(a:float, b:float, *args)->float:
    valores = [a,b]+list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args)/(len(args)+2)

a = float(input('Entre com um valor: '))
b = float(input('Entre com um valor: '))
c = float(input('Entre com um valor: '))

print('Soma: ', soma(a,b,c))
print('Media: ', media(a,b,c))
#%%
#kwargs
def calc_imposto(preco:float, tx_base=1.0, **kwargs):
    imposto =  preco * tx_base
    for i in kwargs:
        print(i, kwargs[i])
        imposto *= kwargs[i]
    return imposto

dict_impostos = {
    'municipal': 0.5,
    'estadual': 0.5
}
#print(calc_imposto(10, municipio=0.5, novo=0.5))
print(calc_imposto(100, 0.5, **dict_impostos, internacional=0.5))