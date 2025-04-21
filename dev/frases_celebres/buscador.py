import csv
import sys

def cargar_frases(nombre_archivo):
    frases = []
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if len(fila) == 2:
                frase = fila[0].strip().strip('"')
                pelicula = fila[1].strip().strip('"')
                frases.append((frase, pelicula))
    return frases

def buscar_por_palabras(frases, palabras):
    resultados = []
    encontrados = set()
    palabras = [p.lower() for p in palabras]

    for palabra in palabras:
        for frase, pelicula in frases:
            if palabra in frase.lower():
                clave = (frase, pelicula)
                if clave not in encontrados:
                    resultados.append(clave)
                    encontrados.add(clave)
    return resultados

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python buscador.py palabra1 [palabra2 ... palabraN]")
        sys.exit(1)

    palabras = sys.argv[1:]
    frases = cargar_frases("frases.csv")
    resultados = buscar_por_palabras(frases, palabras)

    if resultados:
        print(f"\nFrases que contienen alguna de las palabras: {', '.join(palabras)}\n")
        for frase, pelicula in resultados:
            print(f"\"{frase}\" - {pelicula}")
    else:
        print(f"\nNo se encontraron frases con ninguna de las palabras: {', '.join(palabras)}")
