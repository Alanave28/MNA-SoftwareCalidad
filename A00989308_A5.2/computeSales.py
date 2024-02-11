# pylint: disable=C0103
"""Código que calcula el costo total de todas las ventas"""

import sys
import time
import json
import locale

TOTAL_COSTOS = 0

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

if len(sys.argv) != 3:
    print("Utilizar el comando: python computeSales.py "
          + "<archivo_productos> <archivo_ventas>")
    sys.exit(1)

cost_file = sys.argv[1]
sales_file = sys.argv[2]
inicio = time.time()

try:
    if '%.json' in cost_file or '%.JSON' in cost_file:
        print("La lista de productos no cumple con lo requerido, "
              + "favor de cargar archivo con extensión json.")
        sys.exit(1)

    if '%.json' in sales_file or '%.JSON' in sales_file:
        print("La lista de ventas no cumple con lo requerido, "
              + "favor de cargar archivo con extensión json.")
        sys.exit(1)

    try:
        with open(cost_file, 'r', encoding="utf-8") as j:
            dict_costos = json.loads(j.read())
    except FileNotFoundError:
        print(f"Error: Archivo '{cost_file}' no encontrado.")
        sys.exit(1)

    try:
        with open(sales_file, 'r', encoding="utf-8") as j:
            dict_ventas = json.loads(j.read())
    except FileNotFoundError:
        print(f"Error: Archivo '{sales_file}' no encontrado.")
        sys.exit(1)

    for sale in dict_ventas:
        for item in dict_costos:
            try:
                if sale['Product'] == item['title']:
                    TOTAL_COSTOS += sale['Quantity']*item['price']
            except ValueError:
                print(f"ALERTA: Valor inválido: '{sale['SALE_ID']}'")

    TOTAL_COSTOS = locale.currency(TOTAL_COSTOS, grouping=True)
    fin = time.time()
    tiempo_exec = round(fin - inicio, 4)

    print(f"\nTOTAL COSTOS: {TOTAL_COSTOS}\n")
    print(f"TIEMPO DE EJECUCIÓN: {tiempo_exec} seconds\n")

    with open("SalesResults.txt", 'w', encoding='utf-8') as archivoFinal:
        archivoFinal.write(f"TOTAL COSTOS: {TOTAL_COSTOS}\n")
        archivoFinal.write(f"TIEMPO DE EJECUCIÓN: {tiempo_exec} seconds\n")

except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
