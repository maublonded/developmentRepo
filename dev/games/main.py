'''Programa principal de games'''
from athlete import athlete
from sport import sport
from team import team
from game import Game
import json
 
def main(archivo_torneo:str):
    '''Función principal de games'''
    if archivo_torneo != "":
        with open(archivo_torneo, "r", encoding="UTF8") as f:
            torneo = json.load(f)
    else:
        players_mexico = ['Chicharito','Chucky','Ochoa','Guardado','Herrera','Jimenez','Tecatito','Gallardo','Salcedo','Moreno','Layun']
        players_españa = ['Ramos','Iniesta','Casillas','Xavi','Torres','Villa','Pique','Alba','Busquets','Pedro','Silva']
        lista_mexico = [athlete(x) for x in players_mexico]
        lista_españa = [athlete(x) for x in players_españa]
        soccer = sport("Soccer", 11, "FIFA")
        mexico = team("Mexico", soccer, lista_mexico)
        españa = team("España", soccer, lista_españa)
        juego = Game(mexico, españa)
        torneo = [juego.to_json()]
        archivo = "torneo.json"
        with open(archivo, "w", encoding="UTF8") as f:
            json.dump(torneo, f, ensure_ascii=False ,indent=4)
        print(f"Se escribió el archivo {archivo} Satistactoriamente")
        
        # Jugar todos los juegos del torneo
    for juego in torneo:
        A = team(juego['A']['name'], sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [athlete(x['name']) for x in juego['A']['players']])
        B = team(juego['B']['name'], sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo_torneo = "torneo.json"
    main(archivo_torneo)
 