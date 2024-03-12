import streamlit as st
from boes_comunidades.galicia import boe_galicia
from bs4 import BeautifulSoup


st.title('Fandit Subvenciones')
st.write('Bienvenido a Fandit Subvenciones, una aplicación que te ayudará a encontrar subvenciones para tu proyecto.')

# Datos de las subvenciones
datos_boe = []
mensaje = ''
datos_galicia = []
# Palabras a verificar
palabras_a_verificar = ["subvención", "extracto", "BDNS", "transitoria"]

def get_datos_fecha(fecha):
    # Obtener el día y llenar con ceros a la izquierda si es necesario
    dia_fecha = str(fecha.day).zfill(2)

    # Obtener el mes y llenar con ceros a la izquierda si es necesario
    mes_fecha = str(fecha.month).zfill(2)

    anno_fecha = str(fecha.year)

    # Devolver las cadenas formateadas
    return dia_fecha, mes_fecha, anno_fecha

with st.form(key='form'):
    fecha_elegida = st.date_input("Seleccione la fecha para buscar:")
    boton_submit = st.form_submit_button("Consultar")
    # Ejecutamos la accion de submit con el boton
    if boton_submit:
        dia, mes, anno = get_datos_fecha(fecha_elegida)

        # Datos del BOE
        # datos_boe, mensaje = boe_data(dia, mes, anno, palabras_a_verificar)

        # Datos del BOE: GALICIA
        datos_galicia, url_encontrada = boe_galicia(dia, mes, anno, palabras_a_verificar)
        print(datos_galicia)

# Fuera del Formulario
st.write("<strong>Fecha seleccionada: </strong>", fecha_elegida, unsafe_allow_html=True)

if datos_galicia:
    st.header("Subvenciones de GALICIA")
    st.write(f"Para el día: {dia}/{mes}/{anno}, se han econtrado las siguientes palabras")
    for termino in datos_galicia:
        st.write(termino)
    st.write(f"Este es el link al BOE: [link]({url_encontrada})")

else:
    st.header("Subvenciones de GALICIA")
    st.write(f"Este día no se han encontrado las palabras: {palabras_a_verificar} para GALICIA Comunidad")