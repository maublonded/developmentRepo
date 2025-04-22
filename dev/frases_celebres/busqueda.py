''' Programa que busca una lista en las frases celebres de peliculas '''

import os 
import csv
import argparse

# Funcion para leer el archivo CSV y devolver una lista de frases
def leer_csv(archivo):
    ''' Lee un archivo CSV y devuelve una lista de frases '''
    frases = []
    with open(archivo, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            frases.append(fila[0])
    return frases

# Funcion para buscar palabras en las frases
def buscar_palabras(frases,palabras):
    ''' Busca palabras en una lista de frases '''
    resultados = []
    for frase in frases:
        for palabra in palabras:
            if palabra.lower() in frase.lower():
                resultados.append(frase)
                break
    return resultados

# Funcion para mostrar las frases encontradas
def mostrar_frases(frases):
    ''' Muestra las frases encontradas '''
    for frase in frases:
        print(frase)

# Funcion principal que ejecuta el programa
def main(archivo,lista_palabras):
    ''' Funcion principal que ejecuta el programa '''
    # Leer el archivo CSV
    frases = leer_csv(archivo)

    # Buscar las palabras en las frases
    resultados = buscar_palabras(frases, lista_palabras)

    # Mostrar las frases encontradas
    print(frases)
    mostrar_frases(resultados)

if __name__ == '__main__':
    # Crear el parser
    parser = argparse.ArgumentParser(description='Buscar palabras en frases celebres de peliculas.')

    # Añadir argumentos
    parser.add_argument('palabras', nargs='+', help='Palabras a buscar en las frases.')

    #Parsear los argumentos
    args = parser.parse_args()
    archivo_frases = os.path.join(os.path.dirname(__file__), 'frases.csv')

    # Llamar a la funcion principal
    main(archivo_frases, args.palabras)