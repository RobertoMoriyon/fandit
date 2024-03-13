import requests
from bs4 import BeautifulSoup

def buscar_terminos_en_pagina(url, palabras_buscar):
    # Obtain the HTML content of the page
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        html_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining the page: {e}")
        return

    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    terminos_encontrados = []

    for termino in palabras_buscar:
        if soup.body and termino.lower() in soup.body.get_text().lower():
            terminos_encontrados.append(termino)

    return terminos_encontrados


def boe_murcia(dia_boe, mes_boe, anno_boe, palabras):
    url = (f'https://www.borm.es/#/home/sumario/{dia_boe}-{mes_boe}-{anno_boe}')
    terminos = buscar_terminos_en_pagina(url, palabras)
    return terminos, url


