import streamlit as st
import pandas as pd
from utils import predict_flores

# Título de la aplicación
st.title('Predicción manual de rotura de stock')
st.image('demanda.jpg', caption='Imagen de iris', use_column_width=True)

# Texto introductorio
st.write('**Ingresa los datos manualmente para realizar la predicción de la rotura de stock**')

# Diccionario para almacenar los datos de entrada
input_data = {}

# Lista de columnas para las características de la flor
columns = ['stock actual', 'ventas recientes', 'tiempos estimado de reposicion ', 'tipo de producto']

# Bucle para recorrer las columnas y obtener los datos de entrada
for col in columns:
    # Widget de entrada numérica para cada característica
    input_data[col] = st.number_input(col, value=0.0)

st.sidebar.header("Parametros del usuario")

# Botón para realizar la predicción
if st.button('Realizar Predicción'):
    # Convertir el diccionario de entrada a un DataFrame de una sola fila
    input_df = pd.DataFrame([input_data])

    # Realizar la predicción utilizando la función predict_flores
    predicted_value = predict_flores(input_df)

    # Mostrar el resultado de la predicción
    st.success('Éxito al realizar la predicción!')
    st.write('El resultado de la predicción es:', predicted_value[0])