import streamlit as st
import pandas as pd
from pathlib import Path

COMISSAO = 0.08

def leitura_dw_dados():
    if not 'dados' in st.session_state:
        caminho = Path(__file__).parents[0] / "datasets" 
        df_vendas = pd.read_csv(caminho / "vendas.csv", sep=';', decimal = ',', index_col=0, parse_dates=True)
        df_filiais = pd.read_csv(caminho / "filiais.csv", sep=';', decimal = ',', index_col=0, parse_dates=True)
        df_produtos = pd.read_csv(caminho / "produtos.csv", sep=';', decimal = ',', index_col=0, parse_dates=True)
        dados = {
            'df_vendas': df_vendas, 
            'df_filiais': df_filiais, 
            'df_produtos': df_produtos
            }
        
        st.session_state['dados'] = dados
        st.session_state['caminho_datasets'] = caminho
       


