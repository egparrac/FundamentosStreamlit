import streamlit as st

st.title("Eres estupida NAYLA")
st.sidebar.image("LogoUHEpng.png")
st.sidebar.title("Parámetros")




monto = st.number_input("Ingrese el monto de su prestamo", value = 5000)
interes = st.number_input("Ingrese el interes")
tiempo_meses = st.number_input("Ingrese el tiempo en meses")
resultado = monto*interes*(tiempo_meses/12)

st.write("El resultado es:", resultado)
