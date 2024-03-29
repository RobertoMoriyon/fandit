import streamlit as st
from boes_comunidades.galicia import boe_galicia
from boes_comunidades.rioja import boe_rioja
from boes_comunidades.castilla_leon import boe_castilla_leon
from boes_comunidades.castilla_mancha import boe_castilla_mancha
from boes_comunidades.murcia import boe_murcia
from boes_comunidades.extremadura import boe_extremadura
from boes_provincias.alava import boe_alava
from boes_provincias.gipuzkoa import boe_gipuzkoa
from boes_provincias.pontevedra import boe_pontevedra
from boes_provincias.coruna import boe_coruna
from boes_provincias.ourense import boe_ourense
from boes_provincias.valladolid import boe_valladolid
from boes_provincias.salamanca import boe_salamanca
from boes_provincias.avila import boe_avila

from bs4 import BeautifulSoup

st.title('Fandit')
st.write('Selecciona una fecha para buscar subvenciones en los boletines de las comunidades y provincias.')

# Boton Submit no activo
boton_submit= False

# Datos de las subvenciones
datos_boe = []
mensaje = ''
datos_galicia = []
datos_castilla_leon = []
datos_castilla_mancha = []
datos_murcia = []
datos_extremadura = []
datos_alava = []
datos_gipuzkoa = []
datos_pontevedra = []
datos_coruna = []
datos_ourense = []
datos_valladolid = []
datos_salamanca = []
datos_avila = []

# Palabras a verificar
palabras_a_verificar = ["subvención", "extracto", "BDNS", "subvenciones", "subven"]

def get_datos_fecha(fecha):
    # Obtener el día y llenar con ceros a la izquierda si es necesario
    dia_fecha = str(fecha.day).zfill(2)

    # Obtener el mes y llenar con ceros a la izquierda si es necesario
    mes_fecha = str(fecha.month).zfill(2)

    anno_fecha = str(fecha.year)

    # Devolver las cadenas formateadas
    return dia_fecha, mes_fecha, anno_fecha

def escribir_datos(provincia,datos, url):
    st.header(provincia)
    st.write(f"✅ <strong>Terminos encontrados:</strong> {datos}, en este boletin: [link]({url})", unsafe_allow_html=True)

with st.form(key='form'):
    fecha_elegida = st.date_input("Fecha para buscar:")
    boton_submit = st.form_submit_button("Consultar")
    # Ejecutamos la accion de submit con el boton
    if boton_submit:
        dia, mes, anno = get_datos_fecha(fecha_elegida)

        # Datos del BOE
        # datos_boe, mensaje = boe_data(dia, mes, anno, palabras_a_verificar)

        # Datos del BO Comunidades:
        datos_galicia, url_galicia = boe_galicia(dia, mes, anno, palabras_a_verificar)
        datos_castilla_leon, url_castilla_leon = boe_castilla_leon(dia, mes, anno, palabras_a_verificar)
        datos_castilla_mancha, url_castilla_mancha = boe_castilla_mancha(dia, mes, anno, palabras_a_verificar)
        datos_extremadura, url_extremadura = boe_extremadura(dia, mes, anno, palabras_a_verificar)
        # datos_murcia, url_murcia = boe_murcia(dia, mes, anno, palabras_a_verificar)
        # datos_rioja, url_rioja = boe_rioja(dia, mes, anno, palabras_a_verificar)
        
        # Datos del BO Provincias:
        datos_alava, url_alava = boe_alava(dia, mes, anno, palabras_a_verificar)
        datos_gipuzkoa, url_gipuzkoa = boe_gipuzkoa(dia, mes, anno, palabras_a_verificar)
        datos_pontevedra, url_pontevedra = boe_pontevedra(dia, mes, anno, palabras_a_verificar)
        datos_coruna, url_coruna = boe_coruna(dia, mes, anno, palabras_a_verificar)
        datos_ourense, url_ourense = boe_ourense(dia, mes, anno, palabras_a_verificar)
        datos_valladolid, url_valladolid = boe_valladolid(dia, mes, anno, palabras_a_verificar)
        datos_salamanca, url_salamanca = boe_salamanca(dia, mes, anno, palabras_a_verificar)
        # datos_avila, url_avila = boe_avila(dia, mes, anno, palabras_a_verificar)

        # Cambiamos boton sumbit a True
        boton_submit = True

# Fuera del Formulario
if boton_submit:        

    st.write("<strong>Fecha seleccionada: </strong>", fecha_elegida, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Comunidades", "Provincias"])

    with tab1:
        if datos_galicia:
            escribir_datos("Galicia", datos_galicia, url_galicia)
        else:
            st.header("Galicia")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")

        if datos_castilla_leon:
            escribir_datos("Castilla y León", datos_castilla_leon, url_castilla_leon)
        else:
            st.header("Castilla y León")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")
        
        if datos_castilla_mancha:
            escribir_datos("Castilla La Mancha", datos_castilla_mancha, url_castilla_mancha)
        else:
            st.header("Castilla La Mancha")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")

        if datos_extremadura:
            escribir_datos("Extremadura", datos_extremadura, url_extremadura)
        else:
            st.header("Extremadura")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")

    with tab2:
        if datos_alava:
            escribir_datos("Alava", datos_alava, url_alava)
        else:
            st.header("Alava")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")

        if datos_gipuzkoa:
            escribir_datos("Gipuzkoa", datos_gipuzkoa, url_gipuzkoa)
        else:
            st.header("Gipuzkoa")
            st.write(f"Este día no se han encontrado las palabras: {palabras_a_verificar}")

        if datos_pontevedra:
            escribir_datos("Pontevedra", datos_pontevedra, url_pontevedra)
        else:
            st.header("Pontevedra")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")

        if datos_coruna:
            escribir_datos("A Coruña", datos_coruna, url_coruna)
        else:
            st.header("A Coruña")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")
        
        if datos_ourense:
            escribir_datos("Ourense", datos_ourense, url_ourense)
        else:
            st.header("Ourense")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")

        if datos_valladolid:
            escribir_datos("Valladolid", datos_valladolid, url_valladolid)
        else:
            st.header("Valladolid")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")

        if datos_salamanca:
            escribir_datos("Salamanca", datos_salamanca, url_salamanca)
        else:
            st.header("Salamanca")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")

        '''Problema porque subvenciones esta en un sub-menu del codigo
        if datos_avila:
            escribir_datos("Ávila", datos_avila, url_avila)
        else:
            st.header("Ávila")
            st.write(f"❌ Este día no se han encontrado las palabras: {palabras_a_verificar}")
        '''