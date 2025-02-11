'''
Funciones auxiliares del juego ahorcado
'''
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

if __name__ == '__main__':
    plantilla = carga_plantillas('layout')
    despliega_plantilla(plantilla,3)
    lista_oraciones = carga_archivo_texto('./data/pg15532.txt')
    print(lista_oraciones[60:70])
    texto = "".join(lista_oraciones[110:00])
    print(texto[:100])
