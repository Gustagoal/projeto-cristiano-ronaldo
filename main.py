import pandas as pd 
import streamlit as st 
import openpyxl , plotly

# url = "https://www.espn.com.br/futebol/jogador/estatisticas/_/id/22774/cristiano-ronaldo"

table = pd.read_excel("dados.xlsx")


st.title("Estaticas por ano")
st.bar_chart(table,x="Ano" ,y=["Gols",'Assistencias',"Titular"] , width=300 , height=400)


