# Paso 4. Desarrollo del cuadro de mandos de la aplicación web

import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    return df

df = load_data()

st.title("Visualización interactiva de venta de vehiculos modelos 1908 a 2019")

# Casilla para histograma
build_histogram = st.checkbox('Construir histograma por kilometraje')

if build_histogram:
    st.write('Histograma por kilometraje')
    fig_hist = px.histogram(
        df,
        x='odometer',
        nbins=30,
        title='Distribución del kilometraje',
        labels={'odometer': 'Kilometraje'}
)

    fig_hist.update_layout(
        yaxis_title='Cantidad de vehículos',
        yaxis=dict(tickformat='d'),  # 'd' = entero
        xaxis=dict(tickformat='d')   # también puedes aplicarlo al eje X si lo deseas
)

    st.plotly_chart(fig_hist)



# Casilla para histograma
build_histogram = st.checkbox('Construir histograma cantidad de vehículos por modelo-año')

if build_histogram:
    st.write('Histograma por modelo-año')

    fig_hist = px.histogram(
        df,
        x='model_year',
        nbins=len(df['model_year'].unique()),  # opcional: un bin por año
        title='Distribución de vehículos por modelo-año',
        labels={'year': 'Año del vehículo'}
    )

    fig_hist.update_layout(
        yaxis_title='Cantidad de vehículos',
        xaxis_title='Año',
        yaxis=dict(tickformat='d'),
        xaxis=dict(tickformat='d')
    )

    st.plotly_chart(fig_hist)


# Casilla para gráfico de dispersión
build_scatter = st.checkbox('Gráfico de dispersión precio vs kilometraje')

if build_scatter:
    st.write('Gráfico de dispersión: precio vs kilometraje')

    fig_scatter = px.scatter(
        df,
        x='odometer',
        y='price',
        color='model',
        title='Precio vs Kilometraje por Modelo',
        labels={
            'odometer': 'Kilometraje',
            'price': 'Precio (USD)',
            'model': 'Modelo'
        }
    )

    fig_scatter.update_layout(
        xaxis=dict(tickformat='d'),
        yaxis=dict(tickformat='d')
    )

    st.plotly_chart(fig_scatter)

    