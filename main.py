import pandas as pd 
import streamlit as st 
import openpyxl , plotly , lxml

# url = r"https://www.365scores.com/pt-br/news/magazine/quantos-gols-cristiano-ronaldo-tem-na-carreira/"

#url_calendario = "https://www.espn.com.br/futebol/time/calendario/_/id/817"

url_portugal = "https://www.espn.com.br/futebol/time/calendario/_/id/482/por"


table = pd.read_html(url_portugal)
tabela = pd.DataFrame(pd.concat([table[0],table[1],table[2],table[3]]),index=None)

tabela.to_excel("calendario_portugal.xlsx")

calendario = pd.read_excel("calendario.xlsx")
calendario_portugal = pd.read_excel("calendario_portugal.xlsx")


df = pd.read_excel("dados.xlsx")

with st.sidebar:
    clube = st.selectbox("Clube", df["Clube"].unique())
    dados = df[df["Clube"] == clube]
    st.metric("Gols ⚽", dados["Gols"].sum())
    st.metric("Jogos 🥅 ", dados["Jogos"].sum())
    media = dados["Gols"].sum() / dados["Jogos"].sum()
    st.metric("Média 📊",f"{media:.2f}")
    
st.title("Meta 🥇: 1.000 Gols")

st.metric("Gols ⚽️",df["Gols"].sum())
st.metric("Jogos 🥅", df["Jogos"].sum())

opcao = st.selectbox(
    "Calendário",
    ["Al-Nassr", "Portugal"],
    index=None,
    placeholder="Selecione um time"
)

if opcao == "Al-Nassr":
    st.table(calendario)
elif opcao == "Portugal":
    st.table(calendario_portugal)
    
img = r"img/Cristiano-Ronaldo-No-Background.png"    
st.image(img)