from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import os
def scrape_mwalemania():
    # Configuración del ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.headless = False  # Si prefieres que no se vea el navegador, ponlo en True

    # Iniciar el navegador con el ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)

    # Abrir la URL
    url = "https://www.bka.de/SiteGlobals/Forms/Suche/Fahndungsliste_Personenfahndung_Formular.html?nn=4210&cl2Categories_Art=bekannte_person&activeTab=1"
    driver.get(url)

    # Esperar un poco para que la página cargue
    time.sleep(3)

    # Aceptar las cookies
    try:
        # Hacer clic en el botón de aceptar cookies usando el XPath proporcionado
        cookie_button = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div/div/div[4]/div/p/button[2]")
        cookie_button.click()
        print("Botón de cookies aceptado.")
    except Exception as e:
        print(f"Error al hacer clic en el botón de cookies: {e}")

    # Esperar un poco después de hacer clic en el botón de cookies
    time.sleep(2)

    # Hacer clic en el botón "Alle anzeigen" (usando el texto)
    try:
        # Buscar el botón que contiene el texto "Alle anzeigen"
        all_show_button = driver.find_element(By.XPATH, "//*[text()='Alle anzeigen']")
        all_show_button.click()
        print("Botón 'Alle anzeigen' presionado.")
    except Exception as e:
        print(f"Error al hacer clic en el botón 'Alle anzeigen': {e}")

    # Esperar un poco después de hacer clic en el botón "Alle anzeigen"
    time.sleep(2)

    # Extraer todos los elementos dentro de 'js-fahdungsliste-searchresult'
    search_results = driver.find_element(By.CLASS_NAME, "js-fahdungsliste-searchresult")

    # Encuentra todos los elementos 'js-dynamiclist-element' dentro del contenedor principal
    personas = search_results.find_elements(By.CLASS_NAME, "js-dynamiclist-element")

    # Lista para almacenar la información de las personas
    datos_personas = []

    # Instanciar ActionChains para simular el movimiento del mouse
    actions = ActionChains(driver)

    # Extraemos los datos de cada persona
    for persona in personas:
        try:
            # Encontrar la imagen dentro del contenedor de la persona
            foto = persona.find_element(By.XPATH, ".//div[@class='imageContainer']/img")
            
            # Mover el mouse sobre la foto para activar los datos emergentes
            actions.move_to_element(foto).perform()

            # Esperar un poco para que se muestren los datos
            time.sleep(2)

            # Extraer el nombre (familia y primer nombre)
            nombre_familia = persona.find_element(By.XPATH, ".//span[@class='frameBox__familienname']").text if persona.find_elements(By.XPATH, ".//span[@class='frameBox__familienname']") else "N/A"
            nombre_primero = persona.find_element(By.XPATH, ".//span[@class='frameBox__vorname']").text if persona.find_elements(By.XPATH, ".//span[@class='frameBox__vorname']") else "N/A"
            nombre = f"{nombre_familia}, {nombre_primero}"

            # Extraer los detalles del crimen
            delito = persona.find_element(By.XPATH, ".//span[contains(text(), 'Delikt')]/following-sibling::span").text if persona.find_elements(By.XPATH, ".//span[contains(text(), 'Delikt')]/following-sibling::span") else "N/A"
            lugar_crimen = persona.find_element(By.XPATH, ".//span[contains(text(), 'Tatort')]/following-sibling::span").text if persona.find_elements(By.XPATH, ".//span[contains(text(), 'Tatort')]/following-sibling::span") else "N/A"
            fecha_crimen = persona.find_element(By.XPATH, ".//span[contains(text(), 'Tatzeit')]/following-sibling::span").text if persona.find_elements(By.XPATH, ".//span[contains(text(), 'Tatzeit')]/following-sibling::span") else "N/A"

            # Obtener la URL de la foto
            foto_url = foto.get_attribute('src') if foto else "N/A"

            # Guardar la información de cada persona
            datos_personas.append([nombre, delito, lugar_crimen, fecha_crimen, foto_url])

        except Exception as e:
            print(f"Error al extraer datos de una persona: {e}")

    # Crear un DataFrame de pandas para almacenar los datos
    df = pd.DataFrame(datos_personas, columns=["Nombre", "Delito", "Lugar del crimen", "Fecha del crimen", "Foto_URL"])
    
    # Asegurarse de que la carpeta 'data' exista
    os.makedirs(os.path.join(os.path.dirname(__file__), 'data'), exist_ok=True)

    # Exportar los datos a un archivo Excel
    df.to_excel(os.path.join(os.path.dirname(__file__), 'data', 'Mas_buscados_Alemania.xlsx'), index=False)

    print("Los datos se han exportado correctamente a un archivo Excel.")

    # Cerrar el navegador
    driver.quit()

if __name__ == "__main__":
    scrape_mwalemania()