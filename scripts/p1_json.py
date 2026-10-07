import json

texto = '{"codigo":"INI-001", "activa":true, "intereses":["Validar mercado"]}'

try:
    datos = json.loads(texto)

    print("JSON leído correctamente")
    print("Código:", datos["codigo"])
    print("Activa:", datos["activa"])
    print("Tipo de código:", type(datos["codigo"]).__name__)
    print("Tipo de activa:", type(datos["activa"]).__name__)

except json.JSONDecodeError as error:
    print("Error al leer el JSON:")
    print(error)