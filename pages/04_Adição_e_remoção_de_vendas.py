import streamlit as st
import pandas as pd
from pathlib import Path
from utilidades import leitura_dw_dados
from datetime import datetime
import ast

leitura_dw_dados()


df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

df_filiais['cidade/estado'] = df_filiais['cidade'] + '/' + df_filiais['estado']
cidades_filiais = df_filiais['cidade/estado'].unique().tolist()
filial_selecionada = st.sidebar.selectbox('Selecione a cidade/estado da filial:', cidades_filiais, key='cidade_filial')
vendedor_selecionado = st.sidebar.selectbox('Selecionar o vendedor', df_filiais[df_filiais['cidade/estado'] == filial_selecionada]['vendedores'].apply(ast.literal_eval).explode().unique().tolist(), key='selecionar_vendedor')
produtos= df_produtos['nome'].unique().tolist()
produto_selecionado = st.sidebar.selectbox('Selecionar o produto', produtos, key='selecionar_produto')
nome_cliente = st.sidebar.text_input('Digite o nome do cliente', key='nome_cliente')
genero_selecionado = st.sidebar.selectbox('Selecionar o gênero do cliente', ['Masculino', 'Feminino'], key='selecionar_genero')
formas_pagameno = st.sidebar.selectbox('Selecionar a forma de pagamento', df_vendas['forma_pagamento'].unique().tolist(), key='selecionar_forma_pagamento')
adicionar_venda = st.sidebar.button('Adicionar venda', key='adicionar_venda')
if adicionar_venda:
    lista_adicionar = [
                        df_vendas['id_venda'].max() +1,
                        filial_selecionada.split('/')[0],
                        vendedor_selecionado,
                        produto_selecionado,
                        nome_cliente,
                        genero_selecionado,
                        formas_pagameno
                      ]
    
    hora_adicinar = datetime.now()
    df_vendas.loc[hora_adicinar] = lista_adicionar
    caminho_datasets = st.session_state['caminho_datasets']
    df_vendas.to_csv(caminho_datasets / 'vendas.csv', decimal=',', sep=';')
    st.dataframe(df_vendas)

st.sidebar.markdown('## Remoção de vendas')
id_remocao = st.sidebar.number_input('Id venda a ser removido', 0,df_vendas['id_venda'].max())
remover_venda = st.sidebar.button('Remover venda', key='remover_venda')
if remover_venda:
    df_vendas = df_vendas[df_vendas['id_venda'] != id_remocao]
    caminho_datasets = st.session_state['caminho_datasets']
    df_vendas.to_csv(caminho_datasets / 'vendas.csv', decimal=',', sep=';')
    st.session_state['dados']['df_vendas'] = df_vendas
    st.dataframe(df_vendas)
st.dataframe(df_filiais)
st.dataframe(df_produtos)
