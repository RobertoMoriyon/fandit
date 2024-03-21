# https://bop.sede.diputaciondevalladolid.es/ultimobop?p_p_id=BOPVisualizaBoletin_WAR_BOPVisualizaBoletin&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=3&_BOPVisualizaBoletin_WAR_BOPVisualizaBoletin_fecha=2024-03-20

import requests
from bs4 import BeautifulSoup

def buscar_terminos_en_pagina(url, palabras_buscar):
    # Obtener el contenido HTML de la página
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return

    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Buscar los términos en el texto de la página
    terminos_encontrados = []

    for termino in palabras_buscar:
        if soup.body and termino.lower() in soup.body.get_text().lower():
            terminos_encontrados.append(termino)

    return terminos_encontrados


def boe_valladolid(dia_boe, mes_boe, anno_boe, palabras):
    url = (f'https://bop.sede.diputaciondevalladolid.es/ultimobop?p_p_id=BOPVisualizaBoletin_WAR_BOPVisualizaBoletin&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=3&_BOPVisualizaBoletin_WAR_BOPVisualizaBoletin_fecha={anno_boe}-{mes_boe}-{dia_boe}')
    terminos = buscar_terminos_en_pagina(url, palabras)
    return terminos, url