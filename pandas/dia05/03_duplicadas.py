#%%
import pandas as pd

df = pd.DataFrame(
    {
        'nome': ['De', 'Si', 'Ca', 'He', 'De'],
        'sobrenome': ['mi', 'mo', 'mi', 'nan', 'mi'],
        'sal': [1250, 1450, 1500, 1600, 2000]
    }
)
df
#%%
df.drop_duplicates() # elimina a ultima duplicata
# df.drop_duplicates(keep='last') # deixa só a ultima e elimina todas as outras
#%%
df = df.sort_values('sal', ascending=False)
df.drop_duplicates(keep='first', subset=['nome', 'sobrenome'])