'''
    Clase Team:Equipo
'''
from athlete import athlete
from sport import sport

class team:
    '''Clase para representar un equipo'''
    def __init__(self, name:str, sport:sport):
        self.name = name
        self.sport = sport
        self.players = []
    
    def add_player(self, player:athlete):
        '''Agregar un jugador al equipo'''
        self.players.append(player)
    
    def __str__(self):
        return f"Team: {self.name}, {self.sport}"
    
    def __repr__(self):
        return f"Team(name= '{self.name}', sport= {self.sport})"
    
    def to_json(self)->dict:
        '''Convertir Team a JSON'''
        return {"name":self.name, "sport":self.sport.to_json(), "players":[p.to_json() for p in self.players]}
    
if __name__ == "__main__":
    a1 = athlete("Michael Jordan")
    a2 = athlete("Kobe Bryant")
    a3 = athlete("Lebron James")
    a4 = athlete("Stephen Curry")
    a5 = athlete("Shaquille O'Neal")
    s = sport("Basketball", 5, "NBA")
    lakers = team("Los angeles Lakers", s, [a1, a2, a3, a4, a5])
    print(lakers)
    print(repr(lakers))