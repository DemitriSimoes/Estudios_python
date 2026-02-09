#%%
#dicionario são pares de chaves->valor

dict_persona = {
    'nombre': 'Demitri',
    'apelido': 'Simoes',
    'casado': True,
    'formacion': [
        'Electronica', 
        'Adm empresas',
        'CTFL'],
    'cargos': [
        {'nome': 'estag', 'empresa': 'Stc'},
        {'nome': 'junior', 'empresa': 'Stl'},
        {'nome': 'senior', 'empresa': 'Mvd'},
        {'nome': 'pleno', 'empresa': 'Mvd'}
    ]
    }
#%%
print(dict_persona.keys())
print(dict_persona.values())
print(dict_persona.items())

for i in dict_persona.keys():
    print('chave: ', i)
for i in dict_persona.values():
    print('valor: ', i)
for i in dict_persona.items():
    print('item: ', i)
#%%
for i, j in dict_persona.items(): #melhor forma
    print('chave: ', i, '- valor: ', j)
for i in dict_persona.items():
    print(i[0], '->', i[1])
for i in dict_persona:
    print(i, ': ', dict_persona[i])
#%%
print(dict_persona['formacion'][-2:])
print(dict_persona['formacion'][:2])
#%%
print(dict_persona['cargos'][-2]['empresa'])
print(dict_persona['cargos'][-1].values())
for i in dict_persona['cargos'][-1].values():
    print(i)
for i in dict_persona['cargos']:
    print(i['nome'], '-', i['empresa'])
#%%
dict_persona['cargos'][-1]['sal'] = '$5000'
for i in dict_persona['cargos']:
    i['sal']
    print(i)
