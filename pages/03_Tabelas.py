import streamlit as st
import pandas as pd
from pathlib import Path
from utilidades import leitura_dw_dados

leitura_dw_dados()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

st.sidebar.markdown('## Seleção de tabelas')
tabela_selecionada = st.sidebar.selectbox('Selecione a tabela que você deseja ver:', ['Vendas', 'Filiais', 'Produtos'], key='tabela_selecionada')
st.sidebar.divider()
colunas = st.sidebar.multiselect(
    'Selecione as colunas que você deseja ver:', 
    list(df_vendas.columns) if tabela_selecionada == 'Vendas' else list(df_filiais.columns) if tabela_selecionada == 'Filiais' else list(df_produtos.columns),  
    list(df_vendas.columns) if tabela_selecionada == 'Vendas' else list(df_filiais.columns) if tabela_selecionada == 'Filiais' else list(df_produtos.columns)
    )
st.sidebar.divider()
col1,col2 = st.sidebar.columns(2)
coluna_selecionada = col1.selectbox('Filtrar coluna:', colunas, key='coluna_filtro')
valores_unicos_coluna = list(df_vendas[coluna_selecionada].unique() if tabela_selecionada == 'Vendas' else df_filiais[coluna_selecionada].unique() if tabela_selecionada == 'Filiais' else df_produtos[coluna_selecionada].unique()  )
valor_filtro = col2.selectbox('Filtrar valor:', valores_unicos_coluna, key='valor_filtro')
filtrar = col1.button('Aplicar filtro', key='aplicar_filtro')
limpar = col2.button('Limpar', key='limpar_filtro')
if filtrar :
    st.markdown(f'### Tabela: {tabela_selecionada} - Coluna: {coluna_selecionada} - Valor: {valor_filtro}')
    st.dataframe(df_vendas[df_vendas[coluna_selecionada] == valor_filtro] if tabela_selecionada == 'Vendas' else df_filiais[df_filiais[coluna_selecionada] == valor_filtro] if tabela_selecionada == 'Filiais' else df_produtos[df_produtos[coluna_selecionada] == valor_filtro], height=800)
elif limpar:
    st.markdown(f'### Tabela: {tabela_selecionada} - Coluna: {coluna_selecionada} - Valor: {valor_filtro}')
    st.dataframe(df_vendas if tabela_selecionada == 'Vendas' else df_filiais if tabela_selecionada == 'Filiais' else df_produtos, height=800)
else:
    st.markdown(f'### Tabela: {tabela_selecionada} - Coluna: {coluna_selecionada} - Valor: {valor_filtro}')
    st.dataframe(df_vendas if tabela_selecionada == 'Vendas' else df_filiais if tabela_selecionada == 'Filiais' else df_produtos , height=800)