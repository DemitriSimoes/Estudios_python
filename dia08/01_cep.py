#%%
import requests
from tqdm import tqdm

ceps = [
    '58038200',
    '01311902',
    '19060100'
]

url = 'https://viacep.com.br/ws/{cep}/json/'
dados = []
for i in tqdm(ceps, ncols=60, colour='yellow'):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())
print(dados)
#%%
import pandas as pd

dataset = pd.DataFrame(dados)
dataset
#dataset.to_csv('ceps.csv', sep=';') # criou um arquivo csv usando o pandas
#%%
for i in dados[::]:
    for j, k in i.items():
        print(j, '->', k)
    print('*******')
#%%
import json
with open('ceps.json', mode='w', encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)
