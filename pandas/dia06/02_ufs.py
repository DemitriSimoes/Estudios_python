#%%
import requests
import pandas as pd

url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Accept": "text/html"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

df = pd.read_html(response.text)
print(len(df))
#%%

df_uf = df[1]
df_uf.head()
def rpc(x):
    x = x.replace(' ', '').replace(',','.').replace('\xa0','')
    return float(x)
# lista = ['Área (km²)', 'População (Censo 2022)', 'PIB (2015)', 'PIB per capita (R$) (2015)', 'Expectativa de vida (2016)']
df_uf['Área (km²)'] = df_uf['Área (km²)'].apply(rpc)
df_uf['População (Censo 2022)'] = df_uf['População (Censo 2022)'].apply(rpc)
df_uf['PIB (2015)'] = df_uf['PIB (2015)'].apply(rpc)
df_uf['PIB per capita (R$) (2015)'] = df_uf['PIB per capita (R$) (2015)'].apply(rpc)
#%%
def anos(x):
    x = x.replace('anos','').replace(' ','').replace(',','.')
    return float(x)
df_uf['Expectativa de vida (2016)'] = df_uf['Expectativa de vida (2016)'].apply(anos)
#%%
df_uf.head()
df_uf.dtypes
#%%
def alfab(x):
    x = float(x.replace('%','').replace(',','.'))
    x = x/100
    return x
df_uf['Alfabetização (2016)'] = df_uf['Alfabetização (2016)'].apply(alfab)
df_uf.head()
#%%
def classifica(linha):
    return (linha['PIB per capita (R$) (2015)'] > 30000 and
            linha['IDH (2010)'] > 700)

df_uf.apply(classifica, axis=1)
