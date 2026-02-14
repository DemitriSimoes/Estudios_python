#%%
import pandas as pd

df = pd.read_csv('nomedoarquivo', sep=';')

df_stack = (df.set_index(['nome', 'periodo'])
            .stack())
df_stack = df_stack.reset_index()
df_stack.columms = ['nome', 'periodo', 'metrica', 'valor']
df_stack
# o stack serve para empilhar a tabela
# colocar as colunas de metricas em linhas
# e pode selecionar as colunas que serao
# sempre as mesmas com set_index
#%%
# para desempilhar usa-se unstack
df_stack = (df.set_index(['nome',
                          'periodo',
                          'metrica'])
                          .unstack()
                          .reset_index())
#%%
# essa parte eh para eliminar o multinivel de linhas nas colunas
metricas = df_stack.columms.droplevel(0)[2:].tolist()
df_stack.columns = ['nome', 'periodo', metricas]
df_stack