#%%
import pandas as pd

edades = [55,35,46,48,61,28,31,29,39,42,43]
edades = pd.Series(edades)
type(edades)
edades.mean()
edades.sum()
edades.describe()
#%%
df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()
df['flEmail'].count()
df['flEmail'].sum()
df['flEmail'].describe()
#%%
filtro = df.dtypes == 'object'
filtro_redes = df.dtypes[~filtro].keys()
# pode ser feito assim tambem:
# redes_sociais = df.dtype[~(df.dtype == 'objetct')].index.tolist()
redes_sociais = []

for i in filtro_redes:
     redes_sociais.append(i)

redes_sociais
df[redes_sociais].sum()
df[redes_sociais].describe()