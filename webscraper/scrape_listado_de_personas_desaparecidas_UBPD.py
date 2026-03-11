import os
import requests
import json
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL del archivo
url = "https://unidadbusqueda.gov.co/listado-personas-desaparecidas/nombres.js"

# Descargar contenido JS
res = requests.get(url, verify=False)
res.raise_for_status()
data_js = res.text

# Extraer el array de datos
start = data_js.find("[")
end = data_js.rfind("]") + 1
if start == -1 or end == -1:
    raise ValueError("No se encontró el array en el archivo JS")

data_json_str = data_js[start:end]
nombres = json.loads(data_json_str)

# Crear DataFrame
df = pd.DataFrame(nombres)

# Asegurarse de que la carpeta 'data' exista
output_folder = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(output_folder, exist_ok=True)

# Guardar en Excel
output_path = os.path.join(output_folder, 'listado_personas_desaparecidas.xlsx')
df.to_excel(output_path, index=False)

print(f"✅ Excel generado con {len(df)} registros limpios")
