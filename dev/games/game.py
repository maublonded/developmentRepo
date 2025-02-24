# SHE DONT BELIEVE IN SHOOTING STARS BUT SHE BELIEVE IN SHOES AND CARS
# WOOD FLOORS IN THE NEW APARTMENT, COUTURE FROM THE STORE'S DEPARTMENT
# YOU MORE LIKE A LOVE TO START, I'M MORE OF THE TRIPS TO FLORIDA
# ORDER THE HOR D'OEUVRES, VIEWS OF THE WATER, STRAIGHT FROM A PAGE OF YOUR FAVORITE AUTHOR

from Team import Team
from Sport import Sport
from Athlete import Athlete

class Game:
    '''Clase game: Juego entre dos equipos'''
    sports_dict = {
        'LMP' :[x for x in range(0,11)],
        'NBA' :[x for x in range(70,121)],
        'NFL' :[x for x in range(3,56)],
        'LMX' :[x for x in range(0,9)],
    }

    def __init__(self,A:Team,B:Team) -> None:
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0

    def play(self):
        '''Juego simulado entre equipos'''
        for s in self.sports_dict.values():
            print(s)

if __name__ == "__main__":
    dt = ['Jordan','Jhonson','Pipen','Bird','Kobe']
    cz = ['Bjovik','Czack','Pfeizer','Leonard','Kempfe']
    player_a = [Athlete(x) for x in dt]
    player_b = [Athlete(x) for x in cz]
    basketball= Sport("NBA",5,"DreamTeam")
    t = Team("DreamTeam",basketball)
    c = Team("CzackTeam",basketball)
    game = Game(t,c)
    game.play()