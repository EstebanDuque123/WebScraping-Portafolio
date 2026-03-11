import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib3

# Desactivar advertencias por SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_profugos_por_la_justicia_argentina():
    url = "https://www.dnrec.jus.gov.ar/masbuscados"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Obtener contenido HTML (sin verificar el certificado)
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    datos = []
    personas = soup.select('div.col-sm-4')

    for persona in personas:
        nombre = persona.find('h4')
        fecha = persona.find('p')

        nombre_texto = nombre.get_text(strip=True).upper() if nombre else "NO ENCONTRADO"
        fecha_texto = fecha.get_text(strip=True).replace("Prófugo desde: ", "") if fecha else "NO ESPECIFICADO"

        datos.append({
            "NOMBRE": nombre_texto,
            "PRÓFUGO DESDE": fecha_texto
        })

    df = pd.DataFrame(datos)

    # Crear carpeta "data"
    carpeta_data = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(carpeta_data, exist_ok=True)

    # Guardar Excel
    output_path = os.path.join(carpeta_data, 'PROFUGOS BUSCADOS POR LA JUSTICIA - ARGENTINA.xlsx')
    df.to_excel(output_path, index=False)

    print(f"Archivo guardado: {output_path}")

if __name__ == "__main__":
    scrape_profugos_por_la_justicia_argentina()
