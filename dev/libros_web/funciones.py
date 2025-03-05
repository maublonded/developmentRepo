''' Archivo con las funciones necesarias de la Aplicacion libro_web '''

import csv

def leer_archivo_csv(archivo:str)->list:
    ''' Funcion que lee un archivo csv y lo convierte en una lista de diccionarios '''
    with open(archivo, 'r', encoding='utf8') as file:
        return [x for x in csv.DictReader(file)]
    
def crea_diccionario_titulos(lista:list)->dict:
    ''' Funcion que crea un diccionario con los titulos de los libros como clave y el resto de los datos como valores'''
    return {x['titulo']:x for x in lista}

if __name__ == '__main__':
    archivo_csv = 'booklist2000.csv'
    lista_libros = leer_archivo_csv(archivo_csv)
    diccionario_libtos = crea_diccionario_titulos(lista_libros)
    