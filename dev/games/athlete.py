class athlete:
    """ Athlete class with only name attribute """
    def __init__(self, name:str):
        self.name = name

    def __str__(self):
        return f'Athlete: {self.name}'
    
    def __repr__(self):
        return f'Athlete({self.name})'
    
if __name__ == '__main__':
    a = athlete('Usain Bolt')
    a.display()
    print(a) # Athlete: Usain Bolt
    print(repr(a)) # Athlete(Usain Bolt)