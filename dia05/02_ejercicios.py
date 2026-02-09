# solicite ao usuario o nome de uma fruta
# e exiba o preço correspondente
#%%
frutas = [
    ['maça', 1.50],
    ['pera', 1.25],
    ['goiaba', 2.15],
    ['banana', 2.75],
    ['naranja', 0.65],
    ['abacaxi', 3.20],
    ['uva', 1.90],
    ['limon', 1.25],
    ['jaca', 5.80]]
#%%
usuario = input('''
Selecione o número correspondente de tua fruta:
                1. maça
                2. pera
                3. goiaba
                4. banana
                5. naranja
                6. abacaxi
                7. uva
                8. limon
                9. jaca
                número: ''')

if usuario in ['1','2','3','4','5','6','7','8','9']:
    resultado = int(usuario) -1
    print('Escolha: ', frutas[resultado][0], ' $', frutas[resultado][1])
else:
    print('Número inválido!!!')
    
#%%
# solicite ao usuario o nome de uma fruta
# e exiba o preço correspondente
# usando um dicionario

fruta = {    
    '1': ['maça', 1.50],
    '2': ['pera', 1.25],
    '3': ['goiaba', 2.15],
    '4': ['banana', 2.75],
    '5': ['naranja', 0.65],
    '6': ['abacaxi', 3.20],
    '7': ['uva', 1.90],
    '8': ['limon', 1.25],
    '9': ['jaca', 5.80]
}

user = input('''
Selecione o número de tua fruta,
para saber seu preço:
                1. maça
                2. pera
                3. goiaba
                4. banana
                5. naranja
                6. abacaxi
                7. uva
                8. limon
                9. jaca
                número: ''')

if user in ['1','2','3','4','5','6','7','8','9']:
    print('Escolha: ', fruta[user][0], ' $', fruta[user][1])
else:
    print('Número inválido!!!')
#%%
datos = {}

while True:
    frase = input('Entre com uma frase: ')
    if frase == '':
        break
    if frase not in datos:
        datos[frase] = 1
    else:
        datos[frase] += 1

for i, j in datos.items():
    print(i, '-> ', j)