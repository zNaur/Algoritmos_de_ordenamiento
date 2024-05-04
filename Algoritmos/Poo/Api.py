import pandas as pd
import json
import requests
from pandas import json_normalize

ruta = "https://retoolapi.dev/DvxmPF/Musicos_artistas"

datos = requests.get(ruta)
datos = json.loads(datos.text)
datos = json_normalize(datos)
print(datos)

