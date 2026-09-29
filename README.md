# 📊 Analisador de Vendas

Aplicação web desenvolvida em **Python + Streamlit** para análise e gerenciamento de dados de vendas.

O projeto permite visualizar indicadores comerciais, analisar vendas por diferentes dimensões, consultar os datasets utilizados pela aplicação e realizar operações de inclusão e remoção de vendas.

O objetivo principal do projeto é praticar **Python, Pandas, Streamlit, visualização de dados e manipulação de datasets**, criando uma aplicação interativa para análise comercial.

---

## 🚀 Funcionalidades

### 📈 Dashboard de vendas

A aplicação possui um dashboard com indicadores e visualizações para acompanhamento das vendas.

Principais indicadores:

- 💰 Total de vendas
- 📦 Quantidade de produtos vendidos
- 🏢 Principal filial
- 👤 Principal vendedor
- 📅 Comparação com período anterior
- 📈 Evolução das vendas ao longo do tempo
- 🥧 Distribuição das vendas por diferentes dimensões

O usuário pode selecionar um período através das datas inicial e final.

---

### 🔎 Análise dinâmica

A aplicação permite realizar análises utilizando diferentes dimensões dos dados.

Dimensões disponíveis:

- Filial
- Vendedor
- Produto
- Gênero do cliente
- Forma de pagamento

Valores que podem ser analisados:

- Preço
- Comissão

Métricas disponíveis:

- Soma
- Contagem

As análises são realizadas através de **tabelas dinâmicas (Pivot Tables)** utilizando o Pandas.

---

### 🗃️ Consulta dos dados

É possível consultar diferentes conjuntos de dados utilizados pela aplicação:

- Vendas
- Filiais
- Produtos

O usuário pode:

- Selecionar a tabela desejada
- Selecionar as colunas que deseja visualizar
- Filtrar registros por uma coluna específica
- Aplicar filtros
- Limpar os filtros
- Visualizar os dados diretamente na aplicação

---

### ➕ Inclusão de vendas

A aplicação permite adicionar novas vendas informando:

- Filial
- Vendedor
- Produto
- Nome do cliente
- Gênero do cliente
- Forma de pagamento

Após o cadastro, a nova venda é adicionada ao dataset e os dados são persistidos no arquivo `vendas.csv`.

---

### 🗑️ Remoção de vendas

Também é possível remover uma venda informando seu ID.

Após a remoção, o dataset é atualizado e salvo novamente no arquivo `vendas.csv`.

---

## 🛠️ Tecnologias utilizadas

### Linguagem

- **Python 3.14**

### Framework

- **Streamlit**

### Manipulação de dados

- **Pandas**

### Visualização de dados

- **Plotly Express**

### Bibliotecas utilizadas

- `streamlit`
- `pandas`
- `plotly`
- `pathlib`
- `datetime`
- `ast`

---

## 📂 Estrutura do projeto

```text
AnalisadorVendas/
│
├── Home.py
├── utilidades.py
├── requirements.txt
├── README.md
│
└── datasets/
    ├── vendas.csv
    ├── filiais.csv
    └── produtos.csv
```

> A estrutura acima representa a organização esperada do projeto. Os nomes dos arquivos podem variar de acordo com a organização utilizada no ambiente de desenvolvimento.

---

## 📊 Dados utilizados

A aplicação trabalha com três principais conjuntos de dados:

### Vendas

Contém informações relacionadas às vendas realizadas, como:

- ID da venda
- Filial
- Vendedor
- Produto
- Cliente
- Gênero do cliente
- Forma de pagamento
- Data da venda

### Filiais

Contém informações das filiais, como:

- Cidade
- Estado
- Vendedores associados à filial

### Produtos

Contém informações dos produtos, incluindo:

- Nome
- Preço

---

## 💰 Cálculo de comissão

A aplicação utiliza o preço dos produtos para calcular a comissão das vendas.

O preço do produto é obtido através do relacionamento entre os dados de vendas e produtos:

```python
dicionario = df_produtos.set_index('nome')['preco'].to_dict()

df_vendas['preco'] = df_vendas['produto'].map(dicionario)

df_vendas['comissao'] = df_vendas['preco'] * COMISSAO
```

A taxa de comissão é definida através da constante `COMISSAO`, localizada no módulo `utilidades.py`.

---

## 📅 Análise de períodos

O dashboard permite selecionar:

- Data inicial
- Data final

Com essas informações, a aplicação filtra as vendas do período selecionado e também calcula um período anterior para comparação.

Isso permite acompanhar a variação de indicadores como:

- Valor total das vendas
- Quantidade de vendas

---

## 📈 Visualizações

O projeto utiliza diferentes recursos de visualização do Streamlit e Plotly.

### Evolução das vendas

É utilizado um gráfico de linha para apresentar a evolução do valor das vendas ao longo dos dias:

```python
col21.line_chart(df_novo)
```

### Distribuição das vendas

É utilizado um gráfico de pizza para apresentar a distribuição das vendas de acordo com a dimensão selecionada:

```python
fig = px.pie(
    df_vendas,
    names=tipo_analise,
    values='preco'
)
```

---

## 🔄 Gerenciamento dos dados

Os datasets são carregados através da função:

```python
leitura_dw_dados()
```

Os DataFrames são disponibilizados através do `st.session_state`:

```python
df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']
```

Essa estrutura permite compartilhar os dados entre as diferentes páginas/componentes da aplicação.

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/AnalisadorVendas.git
```

Entre na pasta do projeto:

```bash
cd AnalisadorVendas
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Como executar

Para iniciar a aplicação, execute:

```bash
python -m streamlit run Home.py
```

Após iniciar o Streamlit, a aplicação estará disponível no navegador, normalmente em:

```text
http://localhost:8501
```

---

## 📋 Requirements

As dependências do projeto são definidas no arquivo `requirements.txt`.

Exemplo:

```text
streamlit==1.64.0
pandas==VERSÃO
plotly==VERSÃO
```

Para instalar todas as dependências:

```bash
python -m pip install -r requirements.txt
```

---

## 🎯 Objetivo do projeto

O projeto foi desenvolvido com o objetivo de colocar em prática conceitos de desenvolvimento de aplicações para análise de dados utilizando Python.

Durante o desenvolvimento foram trabalhados conceitos como:

- Manipulação de DataFrames com Pandas
- Filtros e agrupamentos
- `groupby`
- `pivot_table`
- `map`
- Cálculos com DataFrames
- Manipulação de datas
- Criação de indicadores
- Gráficos interativos
- Componentes do Streamlit
- `st.session_state`
- Persistência de dados em arquivos CSV
- Organização de funções e módulos
- Interação do usuário com a aplicação

---

## 📚 Principais aprendizados

Este projeto permitiu praticar a construção de uma aplicação de análise de dados do início ao fim, desde a leitura e transformação dos datasets até a criação de uma interface interativa para exploração das informações.

Entre os principais conceitos praticados estão:

- 📊 Análise exploratória de dados
- 🐼 Manipulação de dados com Pandas
- 📈 Visualização de dados
- 🖥️ Desenvolvimento de interfaces com Streamlit
- 🔄 Atualização dinâmica dos dados
- 📁 Leitura e gravação de arquivos CSV
- 🧮 Criação de métricas e indicadores
- 🗂️ Organização de projetos Python

---

## 👨‍💻 Autor

**Bruno do Prado Rocha**

[LinkedIn](www.linkedin.com/in/bruno-do-prado-rocha-16a1711a1)

---

## 📌 Projeto para estudos

Projeto desenvolvido para fins de estudo e prática de **Python, Pandas, Streamlit e análise de dados**.
