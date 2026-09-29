import streamlit as st
import pandas as pd
from pathlib import Path
from utilidades import leitura_dw_dados, COMISSAO

leitura_dw_dados()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']


dicionario = df_produtos.set_index('nome')['preco'].to_dict()
df_vendas['preco'] = df_vendas['produto'].map(dicionario)
df_vendas['comissao'] = df_vendas['preco'] * COMISSAO


COLUNAS_ANALISE = ['filial', 'vendedor', 'produto', 'cliente_genero', 'forma_pagamento']
COLUNAS_VALOR   = [ 'preco', 'comissao']
FUNCOES_AGG = {'soma': 'sum', 'contagem': 'count'}

indices_selecionados = st.sidebar.multiselect('Selecione os indices para analise', COLUNAS_ANALISE)

COLUNAS_ANALISE = [col for col in COLUNAS_ANALISE if col not in indices_selecionados ]
colunas_selecionados = st.sidebar.multiselect('Selecione colunas', COLUNAS_ANALISE)

analise_selecionada = st.sidebar.selectbox('Selecione a analise', COLUNAS_VALOR)

metrica_selecionada = st.sidebar.selectbox('Selecione a metrica', list(FUNCOES_AGG.keys()))

if len(indices_selecionados) > 0 and len(colunas_selecionados) > 0:
    metrica_selecionada = FUNCOES_AGG[metrica_selecionada]
    vendas_pivotadas = pd.pivot_table(df_vendas, index=indices_selecionados, columns=colunas_selecionados, values=analise_selecionada, aggfunc=metrica_selecionada)
    vendas_pivotadas['TOTAL GERAL'] = vendas_pivotadas.sum(axis=1)
    vendas_pivotadas.loc['TOTAL GERAL'] = vendas_pivotadas.sum(axis=0).to_list()
    st.dataframe(vendas_pivotadas, height=500)