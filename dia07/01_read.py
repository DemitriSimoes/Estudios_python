#%%
archivo = 'historia.txt' # caminho do arquivo

abrir_archivo = open(archivo) # abrir arquivo

ler_archivo = abrir_archivo.read() # ler conteudo

print(ler_archivo) # mostrar conteudo

abrir_archivo.close() # fechar arquivo
#%%
# melhor forma de usar um arquivo para não
# esquecer de fechar
archivo = 'historia.txt'
with open(archivo) as usar_archivo:
    conteudo = usar_archivo.read() #quando sai desse escopo ele já fecha

print(conteudo)
#%%
# escrever dentro do arquivo e criar um arquivo

archivo2 = 'historia2.txt'
mensagem = 'Esta eh uma linha de texto.'

with open(archivo2, mode='w') as open_file:
    open_file.write(mensagem)

with open(archivo2, mode='a') as open_file:
    open_file.write('\n Nova linha de texto.')

with open(archivo2) as open_file:
    conteudo = open_file.read()

print(conteudo)