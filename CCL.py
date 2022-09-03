import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

st.title("CCL CALCULATOR")
st.text("App para calcular el valor del dolar contado con liquidación")

acciones = ["BA- THE BOEING COMPANY","TM- TOYOTA","AXP- AMERICAN EXPRESS COMPANY","NKE- NIKE", "PFE- PFIZER","NVDA- NVIDIA CORP", "AZN- ASTRAZENECA","TSLA- TESLA","AAPL- APPLE","JPM-JP MORGAN","YPF- YPF"] 

choice = st.selectbox("Selecciona una acción",acciones).split("-")[0]

if choice == "YPF":
    SYMB_BA = choice+"D.BA"
else:
    SYMB_BA = choice+".BA"

st.text(choice.split("-")[0])
df = yf.download([choice,SYMB_BA], start='2022-01-10', end='2022-05-30', group_by='ticker')
df.dropna(axis=0,inplace =True)
df["CCL"] = df[SYMB_BA]["Close"]/df[choice]["Close"]

st.write("Información más reciente de las acciones")
st.dataframe(df)

st.write("Valores de CCL para la acción ",choice)




st.line_chart(df["CCL"])