import streamlit as st
import pandas as pd
import requests

url = 'https://viacep.com.br/ws/{cep}/json/'

st.title('Busca de cep')

cep = st.text_input('Busque seu cep')

if cep != '':

    try:
        resposta = requests.get(url.format(cep=cep))
        data = pd.DataFrame([resposta.json()])
        st.dataframe(data, hide_index=True)
    
    except Exception as err:
        st.error('Entre com um cep válido!')