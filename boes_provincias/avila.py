# https://www.diputacionavila.es/boletin-oficial/2024/20-03-2024.html

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


def boe_avila(dia_boe, mes_boe, anno_boe, palabras):
    url = (f'https://www.diputacionavila.es/boletin-oficial/{anno_boe}/{dia_boe}-{mes_boe}-{anno_boe}.html')
    terminos = buscar_terminos_en_pagina(url, palabras)
    return terminos, url