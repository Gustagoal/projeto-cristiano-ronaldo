import pandas as pd 
import streamlit as st 
import openpyxl , plotly , lxml

# url = r"https://www.365scores.com/pt-br/news/magazine/quantos-gols-cristiano-ronaldo-tem-na-carreira/"

#table = pd.read_html(url)
#tabela = pd.DataFrame(table[0],index=None)

#tabela.to_excel("dados.xlsx")

import pandas as pd
import streamlit as st

df = pd.read_excel("dados.xlsx")

import pandas as pd
import streamlit as st

df = pd.read_excel("dados.xlsx")

with st.sidebar:
    clube = st.selectbox("Clube", df["Clube"].unique())
    dados = df[df["Clube"] == clube]
    st.metric("Gols", dados["Gols"].sum())
    st.metric("Jogos", dados["Jogos"].sum())
    media = dados["Gols"].sum() / dados["Jogos"].sum()
    st.metric("Média",f"{media:.2f}")
    
st.title("Meta : 1.000 Gols")

st.metric("Gols",df["Gols"].sum())
st.metric("Jogos", df["Jogos"].sum())

img = r"img/Cristiano-Ronaldo-No-Background.png"    
st.image(img)