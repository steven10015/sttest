import streamlit as st
import pandas as pd
from utils import predict_flores

# Título de la aplicación
st.title('Predicción manual de demanda')
st.image('demanda.jpg', caption='Imagen de demanda', use_column_width=True)

# Texto introductorio
st.write('**Ingresa los datos manualmente para realizar la predicción de la demanda:**')

# Diccionario para almacenar los datos de entrada
input_data = {}

# 🔢 ENTRADAS NUMÉRICAS (ENTEROS)
input_data['stock_actual'] = st.number_input(
    'Stock actual',
    min_value=0,
    step=1
)

input_data['ventas_recientes'] = st.number_input(
    'Ventas recientes',
    min_value=0,
    step=1
)

input_data['tiempo_reposicion_dias'] = st.number_input(
    'Tiempo estimado de reposición (días)',
    min_value=0,
    step=1
)

# 📦 CATEGORÍA / DEPARTAMENTO (SELECTBOX)
categoria = st.selectbox(
    'Categoría / Departamento',
    (
        '561 urban hombre',
        '563 casual hombre',
        '582 punto mujer',
        '584 casual mujer',
        '583 basic mujer',
        '586 denim mujer',
        '562 collection mujer'
    )
)

input_data['categoria_departamento'] = categoria

# Sidebar
st.sidebar.header("Parámetros del usuario")

# 🔮 Botón de predicción
if st.button('Realizar Predicción'):
    input_df = pd.DataFrame([input_data])

    predicted_value = predict_flores(input_df)

    st.success('✅ Éxito al realizar la predicción')
    st.write('📈 **Resultado de la predicción:**', predicted_value[0])