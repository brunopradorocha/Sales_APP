import streamlit as st
import pandas as pd
import os
from pathlib import Path
from utilidades import leitura_dw_dados

st.set_page_config(
        page_title="Home", 
        page_icon="🏠", 
        layout="wide")

st.sidebar.markdown("Desenvolvido por [Bruno do Prado Rocha](https://www.linkedin.com/in/bruno-do-prado-rocha-16a1711a1)")
st.markdown("## Bem-vindo ao Analisador de vendas")
st.divider()
st.markdown(''' 
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore ***magna aliqua***. 
    - `pandas`: teste
    - `plotly`: teste
    - `streamlit`: teste
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est [laborum](http://www.google.com)."
''')

