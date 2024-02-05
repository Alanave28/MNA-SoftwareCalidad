"""Código que obtiene las estadísticas de una lista de números"""

import sys
import time

NUM_REGISTROS = 0
DATA = []

def calculo_media(data): 
    """Dividir la suma de los números en la lista contra la cantidad de números en la lista"""
    calculo = sum(data)/len(data)
    return calculo

def calculo_mediana(data):
    """Ordena la lista de números"""
    numeros = sorted(data)

    # Calcula la cantidad de elementos en la lista
    total = len(numeros)

    # Determinar si la cantidad de elementos es impar o par
    es_impar = total % 2 != 0

    # Calcular la mediana
    if es_impar:
        calculo = numeros[total // 2]
    else:
        calculo = (numeros[total // 2 - 1] + numeros[total // 2]) / 2

    return calculo 

def calculo_moda(data):
    """Se crea un diccionario para almacenar la frecuencia de cada número"""
    resultado = {}

    # Contar la frecuencia de cada número en la lista
    for numero in data:
        if numero in resultado:
            resultado[numero] += 1
        else:
            resultado[numero] = 1

    # Encontrar el número con la frecuencia más alta
    concurrencia = 0

    for numero, frecuencia in resultado.items():
        if frecuencia > concurrencia:
            calculo = numero
            concurrencia = frecuencia

    return calculo

def calculo_varianza(data, var_media):
    """Calcular la suma de los cuadrados de las diferencias entre cada número y la media"""
    suma_cuadrados = sum((x - var_media) ** 2 for x in data)

    # Calcula la varianza dividiendo la suma de cuadrados por la cantidad de elementos
    calculo = suma_cuadrados / len(data)

    return calculo

def calculo_desviacion_estandar(var_varianza):
    """Calcular la desviación estándar como la raíz cuadrada de la varianza"""
    calculo = var_varianza ** 0.5
    
    return calculo

if len(sys.argv) != 2:
    print("Usage: python computeStatistics.py <file_path>")
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

    media = calculo_media(DATA)
    mediana = calculo_mediana(DATA)
    moda = calculo_moda(DATA)
    varianza = calculo_varianza(DATA, media)
    dvcEstandar = calculo_desviacion_estandar(varianza)

    fin = time.time()

    with open("StatisticsResults.txt", 'w', encoding='utf-8') as archivoFinal:
        archivoFinal.write(f"COUNT: {NUM_REGISTROS}\n")
        archivoFinal.write(f"MEAN: {media}\n")
        archivoFinal.write(f"MEDIAN: {mediana}\n")
        archivoFinal.write(f"MODE: {moda}\n")
        archivoFinal.write(f"VARIANCE: {varianza}\n")
        archivoFinal.write(f"SD: {dvcEstandar}\n")
        archivoFinal.write(f"TIME ELAPSED: {fin - inicio} seconds\n")

    print("Estadísticas descriptivas calculadas exitosamente.")
    print("Resultados guardados en el archivo StatisticsResults.txt.")


except FileNotFoundError:
    print(f"Error: Archivo '{file_path}' no encontrado.")
    sys.exit(1)

except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
