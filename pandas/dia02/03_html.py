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
df_uf.to_csv('df_uf.csv', sep=';', index=False)