# https://sede.diputaciondesalamanca.gob.es/opencms/opencms/sede/BOP/index.jsp?fechaBoletin=2024-03-19

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


def boe_salamanca(dia_boe, mes_boe, anno_boe, palabras):
    url = (f'https://sede.diputaciondesalamanca.gob.es/opencms/opencms/sede/BOP/index.jsp?fechaBoletin={anno_boe}-{mes_boe}-{dia_boe}')
    terminos = buscar_terminos_en_pagina(url, palabras)
    return terminos, url