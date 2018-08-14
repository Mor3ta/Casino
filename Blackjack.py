import random

class  player():
    cartas=random.sample([1, 2, 3, 4, 5,6,7,8,9,10,11,12,13],  2) 
    def __init__(self,nombre,apuesta):
        self.nombre= nombre
        self.carta=self.cartas
        self.apuesta=apuesta
        self.puntos=self.carta[0]+self.carta[1]


Lucero=player("Lucero",500)
print Lucero.carta
print Lucero.puntos

        
        
        
        
