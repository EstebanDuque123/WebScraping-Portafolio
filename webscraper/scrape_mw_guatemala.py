import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Función para obtener nombres y hechos de una página
def obtener_datos(pagina):
    url = f'https://tupista.gt/denuncias/mas-buscados/?sesion=&id=&clave=&pagina={pagina}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    nombres_divs = soup.find_all('div', class_='cbp-l-grid-projects-title text-center')
    hechos_divs = soup.find_all('div', class_='cbp-l-grid-projects-desc text-center')

    nombres = [div.get_text(separator=' ').strip() for div in nombres_divs]
    hechos = [div.get_text(separator=' ').strip() for div in hechos_divs]

    return list(zip(nombres, hechos))

def mwguatemala():
    # Recolectamos datos de todas las páginas
    datos_totales = []
    pagina = 1

    while True:
        print(f"📄 Procesando página {pagina}...")
        datos = obtener_datos(pagina)
        
        # Si no encuentra datos, rompe el loop
        if not datos:
            print("🚫 No hay más datos. Fin del scraping.")
            break
        
        datos_totales.extend(datos)
        pagina += 1

    # Guardar todos los datos en un Excel
    df = pd.DataFrame(datos_totales, columns=['Nombre', 'Hecho'])
    # Asegurarse de que la carpeta 'data' exista
    os.makedirs(os.path.join(os.path.dirname(__file__), 'data'), exist_ok=True)

    # Exportar los datos a un archivo Excel
    df.to_excel(os.path.join(os.path.dirname(__file__), 'data', 'MWGuatemala.xlsx'), index=False)
    
    print("✅ ¡Todos los datos guardados en MWGuatemala.xlsx!")

if __name__ == "__main__":
    mwguatemala()