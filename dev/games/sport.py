class sport:
    ''' Class for Sport games
    '''

    def __init__(self, name:str, players:int, league:str):
        self.name = name
        if isinstance(players, int): #verificamos que players sea un entero
            self.players = players 
        else:
            self.players = int(players) 
        self.league = league

    def __str__(self)->str:
        '''Reperesentacion en string de Sport'''
        return f"Sport: {self.name}, {self.players}, {self.league}"
    

    def __repr__(self)->str:
        '''Reperesentacion en string de Sport'''
        return f"Sport(name= '{self.name}', players= {self.players}, league= '{self.league}')"
    
    def to_json(self)->dict:
        '''Convertir Sport a JSON'''
        return {"name":self.name, "players":self.players, "league":self.league}
    
if __name__ == "__main__":
    s = sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())
    nfl = sport("Football", 11, "NFL")
    lmp = sport("Baseball", 9, "LMP")
    mlb = sport("Baseball", 9, "MLB")
    lmx = sport("Soccer", 11, "Liga MX")
    nba = sport("Basketball", 5, "NBA")
    lista_deportes = [nfl, lmp, mlb, lmx, nba]
    archivo_deportes = "deportes.txt"
    with open(archivo_deportes, "w") as file:
        for d in lista_deportes:
            file.write(repr(d)+"\n")
            sport_list = []
    sport_list = []
    with open(archivo_deportes, "r") as file:
        for line in file:
            d = eval(line)
            sport_list.append(d)
    print(sport_list)
    print(sport_list[0].to_json())
    #Escribir a un archivo JSON
    import json
    archivo_json = "deportes.json"
    #Convertimos los deportes a JSON
    sports_json = [sport.to_json() for sport in sport_list]
    #escribir la lista como un solo arreglo json
    with open(archivo_json, "w") as file:
        json.dump(sports_json, file, indent = 4)
    #leer el archivo json
    with open(archivo_json, "r") as file:
        sports_list_json = json.load(file)
    print(sports_list_json)