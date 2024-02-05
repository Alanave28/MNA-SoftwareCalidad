"""Código que convierte valores decimales a binarios y hexagonal"""

import sys
import time

NUM_REGISTROS = 0
DATA = []

def convierte_binario_hexadecimal(data):
    """Función para calcular binarios y hexadecimal"""
    res_bin = []
    res_hexa = []

    for num in data:
        num_bin = int(num)
        num_hex = int(num)
        bits = ''
        hexa = ''

        if num_bin == 0:
            return '0'
        while num_bin:
            #Determinación binaria
            bits = ('1' if num_bin & 1 else '0') + bits
            num_bin >>= 1

        while num_hex:
            #Determinación hexadeciaml
            residuo = num_hex % 16
            if residuo < 10:
                hexa = chr(residuo + 48) + hexa
            else:
                hexa = chr(residuo + 55) + hexa
            num_hex //= 16

        res_bin.append(bits)
        res_hexa.append(hexa)

    return res_bin, res_hexa


if len(sys.argv) != 2:
    print("Usage: python convertNumbers.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
inicio = time.time()

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for row in file:
            try:
                num = float(row.strip())
                DATA.append(num)
            except ValueError:
                print(f"Warning: Valor inválido encontrado: '{row}'")

        NUM_REGISTROS = len(DATA)

    resul_binarios, resul_hexadeciaml  = convierte_binario_hexadecimal(DATA)

    fin = time.time()

    with open("ConvertionResults.txt", 'w', encoding='utf-8') as archivoFinal:
        archivoFinal.write("ID, NUMBER, BIN, HEX\n")

        for i in range(NUM_REGISTROS):
            archivoFinal.write(f"{i+1}, {DATA[i]}, {resul_binarios[i]}, {resul_hexadeciaml[i]}\n")

        archivoFinal.write(f"TIME ELAPSED: {fin - inicio} seconds\n")

    print("Conversión de números ejecutados exitosamente.")
    print("Resultados guardados en el archivo ConvertionResults.txt")


except FileNotFoundError:
    print(f"Error: Archivo '{file_path}' no encontrado.")
    sys.exit(1)

except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
