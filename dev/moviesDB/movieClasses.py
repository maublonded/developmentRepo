''' Clases para manejar la base de datos de peliculas '''

import csv
import os
from datetime import datetime

class Actor:
    ''' Clase para manejar la informacion de un actor '''
    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, username):
        self.id_estrella        = id_estrella
        self.nombre             = nombre
        self.fecha_nacimiento   = fecha_nacimiento
        self.ciudad_nacimiento  = ciudad_nacimiento
        self.url_imagen         = url_imagen
        self.username           = username

    def to_dict(self):
        ''' Devuelve un diccionario con la información del actor '''
        return {
            'id_estrella': self.id_estrella,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'ciudad_nacimiento': self.ciudad_nacimiento,
            'url_imagen': self.url_imagen,
            'username': self.username
        }
if __name__ == '__main__':
    archivo = "datos/actores.csv"
    actores = {}
    with open(archivo, encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            actor = Actor(**row)
            actores[actor.id_estrella] = actor
    for id_estrella, actor in actores.items():
        print(f"{id_estrella}: {actor.nombre}")