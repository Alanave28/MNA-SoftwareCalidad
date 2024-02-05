import sys
import time

NUM_REGISTROS = 0
DATA = []

def convierte_binario_hexadecimal(data):
    frecuencia = {}

    for palabra in data:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


if len(sys.argv) != 2:
    print("Usage: python convertNumbers.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
inicio = time.time()

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for row in file:
            try:
                num = row.strip()
                DATA.append(num)
            except ValueError:
                print(f"Warning: Valor inválido encontrado: '{row}'")

        NUM_REGISTROS = len(DATA)

    freq = convierte_binario_hexadecimal(DATA)

    fin = time.time()

    with open("fileWithData.txt", 'w', encoding='utf-8') as archivoFinal:
        archivoFinal.write("ROW LABELS, COUNT\n")

        for pal_encontrada, recuento in freq.items():
            archivoFinal.write(f"{pal_encontrada}, {recuento}\n")

        archivoFinal.write(f"GRAND TOTAL: {NUM_REGISTROS}\n")
        archivoFinal.write(f"TIME ELAPSED: {fin - inicio} seconds\n")

    print("Conversión de números ejecutados exitosamente.")
    print("Resultados guardados en el archivo fileWithData.txt")


except FileNotFoundError:
    print(f"Error: Archivo '{file_path}' no encontrado.")
    sys.exit(1)

except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
