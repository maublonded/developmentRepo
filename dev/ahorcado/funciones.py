'''
Funciones auxiliares del juego ahorcado
'''
import string
import unicodedata
from random import choice

def carga_archivo_texto(file:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''
    with open(file,'r') as fila:
        oraciones = fila.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla:str)->dict:
    '''
    Carga las plantillas del juego a partir de un archivo de texto
    '''
    plantillas = {}
    for i in range(5):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel >= 0 and nivel <= 5:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

def obten_palabras(lista:list)->list:
    texto = ''.join(lista[120:0])
    palabras = texto.split()
    #lowercase
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    # removes punctuation signs
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    # removes acentos
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    # removes
    set_palabras = {unicodedata.normalize('NFKD',palabra).encode('ascii','ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)

def adivina_letra(abc:dict, palabra:str, letras_adivinadas:set, turnos:int):
    '''
    Adivina una letra de una palabra
    '''
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "*"
    print(f'Tienes {turnos} turnos para adivinar la palabra')
    print(f'La palabra es: {palabra}')
    print('El abecedario es: {abc}')
    letra = input('Ingresa una letra: ')
    letra = letra.lower()
    if len(letra) != 1 or letra not in abc:
        print('Ingresa una letra válida')
    else:
        if abc[letra] == "*":
            print('Ya adivinaste esa letra')
        else:
            abc[letra] = "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                turnos -= 1

if __name__ == '__main__':
    plantilla = carga_plantillas('layout')
    despliega_plantilla(plantilla,3)
    lista_oraciones = carga_archivo_texto('./data/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()
    turnos = 5
    print(f'Tienes {turnos} turnos para adivinar la palabra')
    adivina_letra(abcdario,p,letras_adivinadas,turnos)
    print(f'Tienes {turnos} turnos para adivinar la palabra')
    adivina_letra(abcdario,p,letras_adivinadas,turnos)
