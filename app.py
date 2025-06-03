import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('notebooks/vehicles_us.csv')  

# Encabezado de la aplicación
st.header('Análisis de vehículos en venta - Aplicación interactiva')

# Botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el odómetro de los vehículos.')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs. odómetro.')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Odómetro y Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)