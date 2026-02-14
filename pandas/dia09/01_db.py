#%%
import pandas as pd
import sqlalchemy
#%%
engine = sqlalchemy.create_engine('sqlite:///../data/olist.db')

clientes = pd.read_sql_table(table_name='tb_customers', con=engine)
clientes.head()
#%%
query = 'SELECT * FROM tb_customers LIMIT 50'

client = pd.read_sql_query(query, con=engine)
client