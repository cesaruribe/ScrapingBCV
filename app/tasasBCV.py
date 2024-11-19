import requests
import json
import time
import random
from bs4 import BeautifulSoup


def traerData():
    """Extrae y retorna los valores de cambio de divisas del BCV en formato JSON."""
    # Constantes
    url = "https://www.bcv.org.ve/"
    listaIds = ["dolar", "euro", "yuan", "lira", "rublo"]
    claseFecha = "date-display-single"
    try:
        #response = requests.get(url, verify=certifi.where())
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Levanta una excepción si hay un error en la solicitud
        time.sleep(random.uniform(2, 5))  # Retraso aleatorio
        soup = BeautifulSoup(response.content, 'html.parser')

        resultados = {}
        for id_div in listaIds:
            div = soup.find('div', id=id_div)
            if div:
                valores = []
                for elemento in div.find_all(['strong', 'span']):
                    valores.append({elemento.name: elemento.text.strip()})
                
                # Buscar fecha hacia arriba en el árbol DOM
                elemento_padre = div.parent
                while elemento_padre:
                    fecha_elemento = elemento_padre.find('span', class_=claseFecha)
                    if fecha_elemento:
                        valores.append({'date': fecha_elemento.text.strip()})
                        break
                    elemento_padre = elemento_padre.parent
                
                resultados[id_div] = valores
            else:
                print(f"No se encontró el div con ID '{id_div}'")

        # Guardar los datos en el caché
        return resultados
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return {}



                    