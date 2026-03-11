import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Función para hacer scraping de una página específica
def scrape_page(page_number):
    # URL de la página a scrappear
    url = f"https://www.tupista.info/mas-buscados/personas/page/{page_number}/"

    # Realizar la solicitud HTTP GET
    response = requests.get(url)

    # Si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar todos los elementos <div> que contienen la clase especificada
        most_wanted_boxes = soup.find_all('div', class_='most-wanted__box-action')

        # Lista para almacenar los resultados
        data = []

        # Iterar sobre los elementos encontrados
        for box in most_wanted_boxes:
            person_data = {}

            # Extraer los datos de cada div
            person_data['firstname'] = box.get('data-firstname', '')
            person_data['lastname'] = box.get('data-lastname', '')
            person_data['alias'] = box.get('data-alias', '')
            person_data['crime'] = box.get('data-crime', '')
            person_data['address'] = box.get('data-address', '')
            person_data['details'] = box.get('data-details', '')
            person_data['photo'] = box.get('data-photo', '')
            person_data['permalink'] = box.get('data-permalink', '')

            # Agregar los datos a la lista
            data.append(person_data)

        return data
    else:
        print(f"Error al acceder a la página {page_number}. Código de estado: {response.status_code}")
        return []

# Número de páginas a iterar (ajústalo según el número total de páginas)
total_pages = 5  # Puedes ajustar este número para obtener más o menos páginas
all_data = []

# Iterar a través de las páginas
for page in range(1, total_pages + 1):
    print(f"Scrapeando página {page}...")
    page_data = scrape_page(page)
    all_data.extend(page_data)  # Añadir los resultados de la página actual a la lista general

# Crear un DataFrame de Pandas con los datos extraídos
df = pd.DataFrame(all_data)
    
# Asegurarse de que la carpeta 'data' exista
os.makedirs(os.path.join(os.path.dirname(__file__), 'data'), exist_ok=True)

# Exportar los datos a un archivo Excel
df.to_excel(os.path.join(os.path.dirname(__file__), 'data', 'MWSalvador.xlsx'), index=False)

print("Los datos se han guardado correctamente en 'MWSalvador.xlsx'.")
