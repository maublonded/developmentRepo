# SHE DONT BELIEVE IN SHOOTING STARS BUT SHE BELIEVE IN SHOES AND CARS
# WOOD FLOORS IN THE NEW APARTMENT, COUTURE FROM THE STORE'S DEPARTMENT
# YOU MORE LIKE A LOVE TO START, I'M MORE OF THE TRIPS TO FLORIDA
# ORDER THE HOR D'OEUVRES, VIEWS OF THE WATER, STRAIGHT FROM A PAGE OF YOUR FAVORITE AUTHOR

from team import team
from sport import sport
from athlete import athlete
from random import choice

class Game:
    '''Clase game: Juego entre dos equipos'''
    sports_dict = {
        'LMP' :[x for x in range(0,11)],
        'NBA' :[x for x in range(70,121)],
        'NFL' :[x for x in range(3,56)],
        'LMX' :[x for x in range(0,9)],
        'FIFA' :[x for x in range(0,9)],
    }

    def __init__(self,A:team,B:team) -> None:
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0

    def play(self):
        '''Juego simulado entre equipos'''
        league = self.A.sport.league
        points = self.sports_dict[league]
        a = choice(points)
        b = choice(points)
        self.score[self.A.name] = a
        self.score[self.B.name] = b

    def __str__(self) -> str:
        ''' Metodo para mostrar case como string '''
        return f"""
        -----------------------
        Game:
        {self.A.name}: {self.score[self.A.name]}
        {self.B.name}: {self.score[self.B.name]}
        -----------------------"""
    
    def __repr__(self) -> str:
        ''' Metodo para mostrar clase como string '''
        return f"Game:(A={repr(self.A)} B={repr(self.B)})"

    def to_json(self):
        ''' Metodo para convertir clase a json '''
        return{"A":self.A.to_json(),"B":self.B.to_json(),"score":self.score}

if __name__ == "__main__":
    dt = ['Jordan','Jhonson','Pipen','Bird','Kobe']
    cz = ['Bjovik','Czack','Pfeizer','Leonard','Kempfe']
    player_a = [athlete(x) for x in dt]
    player_b = [athlete(x) for x in cz]
    basketball= sport("DreamTeam",5,"NBA")
    t = team("DreamTeam",basketball)
    c = team("CzackTeam",basketball)
    game = Game(t,c)
    print(game)
    print(repr(game) + "\n")
    print(game.to_json())
    game.play()
    print(game)