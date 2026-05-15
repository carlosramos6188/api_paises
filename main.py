from fastapi import FastAPI
import requests

app = FastAPI()

URL = "https://restcountries.com/v3.1/all?fields=name,capital,region,population"

@app.get("/")
def inicio():
    return {
        "mensaje": "API de Países funcionando"
    }

@app.get("/paises")
def obtener_paises():

    respuesta = requests.get(URL)

    if respuesta.status_code != 200:
        return {
            "error": "No se pudo obtener información",
            "status": respuesta.status_code
        }

    datos = respuesta.json()

    paises = []

    for pais in datos:

        nombre = "Desconocido"
        capital = "No tiene"
        region = "Sin región"
        poblacion = 0

        # Nombre
        if "name" in pais:
            if "common" in pais["name"]:
                nombre = pais["name"]["common"]

        # Capital
        if "capital" in pais:
            if isinstance(pais["capital"], list):
                if len(pais["capital"]) > 0:
                    capital = pais["capital"][0]

        # Región
        if "region" in pais:
            region = pais["region"]

        # Población
        if "population" in pais:
            poblacion = pais["population"]

        paises.append({
            "nombre": nombre,
            "capital": capital,
            "region": region,
            "poblacion": poblacion
        })

    return paises


@app.get("/paises/region/{region}")
def paises_por_region(region: str):

    respuesta = requests.get(URL)

    if respuesta.status_code != 200:
        return {
            "error": "No se pudo obtener información"
        }

    datos = respuesta.json()

    paises_filtrados = []

    for pais in datos:

        region_pais = pais.get("region", "")

        if region_pais.lower() == region.lower():

            nombre = "Desconocido"
            capital = "No tiene"
            poblacion = 0

            # Nombre
            if "name" in pais:
                if "common" in pais["name"]:
                    nombre = pais["name"]["common"]

            # Capital
            if "capital" in pais and len(pais["capital"]) > 0:
                capital = pais["capital"][0]

            # Población
            if "population" in pais:
                poblacion = pais["population"]

            paises_filtrados.append({
                "nombre": nombre,
                "capital": capital,
                "poblacion": poblacion
            })

    return paises_filtrados

@app.get("/paises/poblacion/{cantidad}")
def paises_por_poblacion(cantidad: int):

    respuesta = requests.get(URL)

    if respuesta.status_code != 200:
        return {
            "error": "No se pudo obtener información"
        }

    datos = respuesta.json()

    paises_filtrados = []

    for pais in datos:

        poblacion = pais.get("population", 0)

        if poblacion >= cantidad:

            nombre = "Desconocido"
            capital = "No tiene"
            region = "Sin región"

            # Nombre
            if "name" in pais:
                if "common" in pais["name"]:
                    nombre = pais["name"]["common"]

            # Capital
            if "capital" in pais and len(pais["capital"]) > 0:
                capital = pais["capital"][0]

            # Región
            if "region" in pais:
                region = pais["region"]

            paises_filtrados.append({
                "nombre": nombre,
                "capital": capital,
                "region": region,
                "poblacion": poblacion
            })

    return paises_filtrados