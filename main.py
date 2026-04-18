import pandas as pd
import streamlit as st
import openpyxl , plotly , lxml

#url_portugal = "https://www.espn.com.br/futebol/time/calendario/_/id/482/por"
url_imagem = "img/png-clipart-cristiano-ronaldo-cristiano-ronaldo-portugal-national-football-team-real-madrid-c-f-fifa-confederations-cup-football-player-portuguese-tshirt-sport-removebg-preview.png"


#table = pd.read_html(url_portugal)
#tabela = pd.concat(table, ignore_index=True)

#tabela.to_excel("calendario_portugal.xlsx")

calendario = pd.read_excel("calendario.xlsx")
calendario_portugal = pd.read_excel("calendario_portugal.xlsx")

df = pd.read_excel("dados.xlsx")

with st.sidebar:
    clube = st.selectbox("Clube", df["Clube"].unique())
    dados = df[df["Clube"] == clube]
    gols = dados["Gols"].sum()
    jogos = dados["Jogos"].sum()
    media = gols / jogos if jogos != 0 else 0
    st.metric("Gols ⚽", gols)
    st.metric("Jogos 🥅 ", jogos)
    st.metric("Média 📊",f"{media:.2f}")

st.title("Meta 🥇: 1.000 Gols")
st.image(url_imagem,width=250)
st.metric("Gols ⚽️",df["Gols"].sum())
st.metric("Jogos 🥅", df["Jogos"].sum())
st.metric("Posição 🎯","Atacante")
st.metric("Idade 🪪" , "41 anos")
st.metric("Nacionalide 🇵🇹"," Portugal")

opcao = st.selectbox(
"Calendário 📆",
["Al-Nassr", "Portugal"],
index=None,
placeholder="Selecione um time"
)

if opcao == "Al-Nassr":
    st.dataframe(calendario,hide_index=True)
elif opcao == "Portugal":
    st.dataframe(calendario_portugal,hide_index=True)
