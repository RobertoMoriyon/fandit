import requests
from bs4 import BeautifulSoup
import time


def buscar_terminos_en_pagina(url, palabras_buscar):
    # Try to obtain the HTML content of the page
    for _ in range(5):  # Retry up to 5 times
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text
            break
        except requests.exceptions.RequestException as e:
            print(f"Error obtaining the page: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)  # Wait for 5 seconds before retrying
    else:
        print("Failed to obtain the page after 5 attempts.")
        return

    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Buscar los términos en el texto de la página
    # terminos_buscar = ["Subvencion", "bdns", "Consellería"]
    terminos_encontrados = []

    for termino in palabras_buscar:
        if termino.lower() in soup.get_text().lower():
            terminos_encontrados.append(termino)

    for a_tag in soup.find_all('a'):
        print(a_tag.get_text())
    # Imprimir resultados
    if terminos_encontrados:
        print(f"Se encontraron los siguientes términos en la página {url}:")
        for termino_encontrado in terminos_encontrados:
            print(f"- {termino_encontrado}")
    else:
        print(f"No se encontraron términos en la página {url}")

    return terminos_encontrados

def boe_rioja(dia_boe, mes_boe, anno_boe, palabras):
    url = (f'https://web.larioja.org/bor-portada?fecha={anno_boe}-{mes_boe}-{dia_boe}')
    print(url)
    terminos = buscar_terminos_en_pagina(url, palabras)
    return terminos, url