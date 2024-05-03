import pandas as pd
import json
import requests
from pandas import json_normalize

ruta = "https://www.datos.gov.co/resource/dyy8-9s4r.json"

datos = requests.get(ruta)
datos = json.loads(datos.text)
datos = json_normalize(datos)
print(datos)

