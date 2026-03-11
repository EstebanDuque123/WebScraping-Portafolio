from playwright.sync_api import sync_playwright
import pandas as pd
import os

def scrape_europol():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://eumostwanted.eu/")

        # Aceptar cookies
        try:
            page.click("#onetrust-accept-btn-handler", timeout=5000)
        except:
            pass

        # Esperar tarjetas
        page.wait_for_selector(".wantedItem")

        items = page.locator(".wantedItem")
        count = items.count()

        datos = []

        for i in range(count):

            try:
                item = items.nth(i)

                # Hover
                item.hover()
                page.wait_for_timeout(800)

                # Nombre
                try:
                    nombre = item.locator(".content").inner_text().strip()
                except:
                    nombre = ""

                # Crimen
                try:
                    crimen = item.locator(".wanted_teaser_quick_info .crime").inner_text().strip()
                except:
                    crimen = ""

                # Estado
                try:
                    estado = item.locator(".wanted_teaser_quick_info .state-of-case").inner_text().strip()
                except:
                    estado = ""

                datos.append({
                    "Nombre": nombre,
                    "Crimen": crimen,
                    "Estado del Caso": estado
                })

                print(f"{i+1}. {nombre} | Crimen: {crimen} | Estado: {estado}")

            except Exception as e:
                print(f"❌ Error en persona #{i+1}: {e}")
                continue

        df = pd.DataFrame(datos)

        # Asegurarse de que la carpeta 'data' exista
        os.makedirs(os.path.join(os.path.dirname(__file__), 'data'), exist_ok=True)

        # Exportar los datos a un archivo Excel
        df.to_excel(
            os.path.join(os.path.dirname(__file__), 'data', 'Europol.xlsx'),
            index=False
        )

        browser.close()

        print("\n✅ Datos guardados en 'Europol.xlsx'")


if __name__ == "__main__":
    scrape_europol()