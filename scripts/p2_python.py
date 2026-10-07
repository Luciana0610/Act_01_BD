iniciativas = [
    {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
    {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
    {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
    {"codigo": "INI-004", "sector": "tecnologia"}
]


def seleccionar_pendientes(registros, sector):
    resultado = []

    for registro in registros:
        if registro.get("sector") == sector and registro.get("pendiente") is True:
            resultado.append(registro["codigo"])

    return resultado


print("Prueba 1 - Con resultados:")
print(seleccionar_pendientes(iniciativas, "tecnologia"))

print("Prueba 2 - Sin resultados:")
print(seleccionar_pendientes(iniciativas, "salud"))
