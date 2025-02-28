''' Programa principal de games '''
from athlete import athlete
from sport import sport
from game import Game
from team import team
import json
import game_logic as gl
 
def main(archivo_torneo:str):
    ''' Funcion principal de game '''
    if archivo_torneo != "":
        with open(archivo_torneo, "r") as file:
            torneo = json.load(archivo_torneo)
    else:
        players_mexico = ['Chicarito','Chucky','Ochoa','Tecatito','Guardado','Herrera','Layun','Moreno','Araujo','Oribe','Gimenez']
        players_espania = ['Casillas','Ramos','Pique','Iniesta','Silva','Isco','Busquets','Costa','Morata','Asensio','Pedri']
        players_brasil = ['Neymar', 'Coutinho', ' Marcelo', 'Casemiro', 'Alisson', 'Jesus', ' Paulinho', 'Thiago', 'Silva', 'Fermino', 'Danilo']
        players_argentina = ['Messi', 'Aguero', 'DiMaria', ' Mascherano', 'Higuain', 'Dybala', 'Otamendi', 'Romero', 'Riquelme', 'Dibu', 'Kempes']
        lista_mexico = [athlete(x) for x in players_mexico]
        lista_espania = [athlete(x) for x in players_espania]
        lista_brasil = [athlete(x) for x in players_brasil]
        lista_argentina = [athlete(x) for x in players_argentina]
        soccer = sport("Soccer", 11, "FIFA")
        mexico = team("Mexico", soccer, lista_mexico)
        espania = team("Espania", soccer, lista_espania)
        brasil = team("Brasil", soccer, lista_brasil)
        argentina = team("Argentina", soccer, lista_argentina)
        equipos = [mexico, espania, brasil, argentina]
        d = {}
        for local in equipos:
            for visitante in equipos:
                if local != visitante:
                    juego = Game(local, visitante)
                    partido = f'{local} - {visitante}'
                    partido_2 = f'{visitante} - {local}'
                    if partido_2  not in d:
                        d[partido] = juego.to_json()
       
        torneo = list(d.values())
        archivo_torneo = "torneo.json"
        with open(archivo_torneo, "w", encoding='utf8') as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
 
        print(f"Se escribio archivo '{archivo_torneo}'satisfactoriamente")
 
    # Jugar todos los juegos del torneo
    for juego in torneo:
        A = team(juego['A']['name'], sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [athlete(x['name']) for x in juego['A']['players']])
        B = team(juego['B']['name'], sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        juego['score'] = game.score
    # Calcular el tablero del puntuacion
    tablero = gl.scoring(torneo)
    gl.display_tablero(tablero)

if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)