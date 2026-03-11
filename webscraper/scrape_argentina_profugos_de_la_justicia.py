import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
def scrape_argentina_profugos_de_la_justicia():
    headers = {'User-Agent': 'Mozilla/5.0'}
    base_url = 'https://www.argentina.gob.ar/seguridad/recompensas/profugos?page='

    nombres = []
    pagina = 1

    while True:
        url = base_url + str(pagina)
        print(f"🔄 Procesando página {pagina}...")

        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            break

        soup = BeautifulSoup(res.text, 'html.parser')
        h4_tags = soup.find_all('h4')

        if not h4_tags:
            print(" No hay más datos.")
            break

        for tag in h4_tags:
            texto = tag.text.strip()
            if texto and texto not in nombres:
                nombres.append(texto)

        pagina += 1

    # Guardar en Excel
    df = pd.DataFrame(nombres, columns=["Nombre"])

    # Asegurarse de que la carpeta 'data' exista
    os.makedirs(os.path.join(os.path.dirname(__file__), 'data'), exist_ok=True)

    # Exportar los datos a un archivo Excel
    df.to_excel(os.path.join(os.path.dirname(__file__), 'data', 'ARGENTINA_PROFUGOS_DE_LA_JUSTICIA.xlsx'), index=False)

    print(" Nombres guardados en 'ARGENTINA_PROFUGOS_DE_LA_JUSTICIA.xlsx'")

if __name__ == "__main__":
    scrape_argentina_profugos_de_la_justicia()