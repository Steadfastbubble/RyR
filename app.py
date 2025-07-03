import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(r'C:\Users\Ferna\OneDrive\Desktop\SPRINT 7\RyR\vehicles_us.csv')

st.header('DataFrame de Vehiculos')

st.dataframe(data=car_data)


hist_button = st.button('Histograma')

if hist_button:
    st.write('Creacion de histograma para el conjunto de datos de anuncios para vehiculos')
    #crear histograma
    fig = px.histogram(car_data, x='odometer')
    #mostrar el grafico
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('grafico de Dispersion')

if scatter_button:
    st.write('Creacion de grafico de dispersion del conjunto de datos vehiculares')
    #se crea el grafico
    fig = px.scatter(car_data, x='odometer')
    #despues se muestra
    st.plotly_chart(fig, use_container_width=True)
