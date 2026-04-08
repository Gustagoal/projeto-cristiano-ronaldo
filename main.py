import pandas as pd 
import streamlit as st 
import openpyxl

# url = "https://www.espn.com.br/futebol/jogador/estatisticas/_/id/22774/cristiano-ronaldo"

table = pd.read_excel("dados.xlsx")

st.title("Estaticas Cristiano Ronaldo")

tabela = table.iloc[0]

if st.button(label="Gols"):
    st.dataframe(tabela["Gols"])


