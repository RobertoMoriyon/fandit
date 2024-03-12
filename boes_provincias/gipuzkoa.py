


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
    # terminos_buscar = ["Subvencion", "bdns", "Consellería"]
    terminos_encontrados = []

    for termino in palabras_buscar:
        if soup.body and termino.lower() in soup.body.get_text().lower():
            terminos_encontrados.append(termino)

    # Imprimir resultados
    if terminos_encontrados:
        print(f"Se encontraron los siguientes términos en la página {url}:")
        for termino_encontrado in terminos_encontrados:
            print(f"- {termino_encontrado}")
    else:
        print(f"No se encontraron términos en la página {url}")

    return terminos_encontrados


def boe_gipuzkoa(dia_boe, mes_boe, anno_boe, palabras):
    # https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/2024/03/11/bc240311.htm
    # https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/2024/03/11/bc240311.htm
    url = (
        f'https://egoitza.gipuzkoa.eus/gao-bog/castell/bog/{anno_boe}/{mes_boe}/{dia_boe}/bc24{mes_boe}{dia_boe}.htm')
    print("gipuzkoa url", url)
    terminos = buscar_terminos_en_pagina(url, palabras)
    return terminos, url