#%%
import random as rd

numero_sorteio = rd.randint(1, 15)
#print(numero_sorteio)

def numero():
    while True:
        
        try:
            numero_usuario = int(input('Digite um número: '))
        except Exception as err:
            print('Entre com valor válido!!')
            continue
        
        if  numero_usuario < 1 or numero_usuario > 15:
            print('Digite um número entre 1 e 15')
        else:
            return numero_usuario
            #break
        
def validacao(usuario, sorteio):
    if usuario == sorteio:
        print('Você acertou, parabéns!!!!!!!!!')
        return True
    elif usuario > sorteio:
        print('Número mais alto, digite um número menor!')
        return False
    else:
        print('Número mais baixo, digite um número maior!')
        return False

for i in range(3):

    n = numero()
    if validacao(usuario=n, sorteio=numero_sorteio):
        break
    
else:
    print('Suas tentativas acabaram!')
