import streamlit as st

st.title('Fandit Subvenciones')

st.write('Bienvenido a Fandit Subvenciones, una aplicación que te ayudará a encontrar subvenciones para tu proyecto.')


with st.form(key='form'):
    fecha_elegida = st.date_input("Seleccione la fecha para buscar:")
    boton_submit = st.form_submit_button("Consultar")
