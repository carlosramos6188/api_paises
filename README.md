# API de Países - FastAPI

## Descripción

Esta API fue desarrollada con FastAPI y consume la API externa REST Countries.

La API permite consultar información de países, filtrando y organizando los datos obtenidos.

---

## API externa utilizada

REST Countries API

https://restcountries.com/

---

## Tecnologías utilizadas

- Python
- FastAPI
- Requests
- Uvicorn

---

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta:

```bash
cd api_paises
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install fastapi uvicorn requests
```

---

## Ejecución

```bash
python -m uvicorn main:app --reload
```

---

## Documentación Swagger

http://127.0.0.1:8000/docs

---

## Endpoints

### Obtener todos los países

```http
GET /paises
```

---

### Obtener países por región

```http
GET /paises/region/{region}
```

Ejemplo:

```http
GET /paises/region/Americas
```

---

### Obtener países por población mínima

```http
GET /paises/poblacion/{cantidad}
```

Ejemplo:

```http
GET /paises/poblacion/50000000
```

---

## Respuestas

La API responde en formato JSON.

Ejemplo:

```json
{
  "nombre": "Colombia",
  "capital": "Bogotá",
  "region": "Americas",
  "poblacion": 50882884
}
```

---

## Autor

Carlos Andres Ramos Peña
Jose de Avila Guette