import streamlit as st
import pandas as pd
import os
from pathlib import Path
from utilidades import leitura_dw_dados, COMISSAO
from datetime import datetime, timedelta
import plotly.express as px

st.set_page_config(
        page_title="Home", 
        page_icon="🏠", 
        layout="wide")

leitura_dw_dados()

selecao_keys = {
                'Filial': 'filial',
                'Vendedor': 'vendedor',
                'Produto': 'produto'
}
df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

dicionario = df_produtos.set_index('nome')['preco'].to_dict()
df_vendas['preco'] = df_vendas['produto'].map(dicionario)
df_vendas['comissao'] = df_vendas['preco'] * COMISSAO

data_inicial = st.sidebar.date_input(
    'Data inicial:',
    value=pd.to_datetime(df_vendas.index.max()).replace(day=1)
)

data_final = st.sidebar.date_input(
    'Data final:',
    value=pd.to_datetime(df_vendas.index.max())
)

st.markdown("### Dashboard de análise")

col1, col2, col3, col4 = st.columns(4)
df_filtrado = df_vendas[
    (df_vendas.index.date >= data_inicial) &
    (df_vendas.index.date <= data_final)
]


data_inicial_anterior = data_inicial - timedelta(days=30)
data_final_anterior = data_final - timedelta(days=30)

# st.write(data_inicial_anterior, data_final_anterior)

df_filtrado_anterior = df_vendas[
    (df_vendas.index.date >= data_inicial_anterior) &
    (df_vendas.index.date <= data_final_anterior)
]

tipo_analise = st.sidebar.selectbox('Selecione uma filia: ', list(selecao_keys.keys()) )
tipo_analise = selecao_keys[tipo_analise]
total_vendas = df_filtrado['preco'].sum()
total_vendas_anterior = df_filtrado_anterior['preco'].sum()
col1.metric(
    "Total de vendas",
    f"R$ {total_vendas:,.2f}",
    (float(total_vendas) - float(total_vendas_anterior)  )
)

Qde_vendida = df_filtrado['produto'].count()
Qde_vendida_anterior = df_filtrado_anterior['produto'].count()
col2.metric(
    "Qde vendida",
    f"{Qde_vendida}",
    (int(Qde_vendida) - int(Qde_vendida_anterior)  )
)

principal_filial  = df_filtrado.groupby('filial')['filial'].count().sort_values(ascending=False).index[0]

col3.metric(
    "Principal filial",
     principal_filial)

principal_vendedor = df_filtrado.groupby('vendedor')['vendedor'].count().sort_values(ascending=False).index[0]

col4.metric(
    "Principal vendedor",
     principal_vendedor)

st.divider()


col21, col22 = st.columns(2)
df_filtrado['dataVenda'] = df_filtrado.index.date
df_novo = df_filtrado.set_index("dataVenda")
df_novo = df_novo.groupby(df_novo.index)['preco'].sum()
col21.line_chart(df_novo)


fig = px.pie(df_vendas, names = tipo_analise, values = 'preco')
col22.plotly_chart(fig)

