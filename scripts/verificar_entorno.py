import os

import numpy as np
import pandas as pd
import faker


print("=== VERIFICACIÓN DEL ENTORNO ===")

print(f"Python funcionando correctamente")
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Faker: {faker.VERSION}")

print("\n=== VERIFICACIÓN DE CARPETAS ===")

carpetas = [
    "data/raw",
    "data/processed",
    "notebooks",
    "outputs",
    "docs",
    "scripts",
    "evidencias",
]

for carpeta in carpetas:
    if os.path.exists(carpeta):
        print(f"[OK] {carpeta}")
    else:
        print(f"[FALTA] {carpeta}")

print("\n=== FIN DE LA VERIFICACIÓN ===")
