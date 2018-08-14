import random

class  player():
    cartas=random.sample([1, 2, 3, 4, 5,6,7,8,9,10,11,12,13],  2) 
    def __init__(self,nombre,dinero,apuesta):
        self.nombre= nombre
        self.carta=self.cartas
        self.dinero=dinero  # cantidad de dinero al iniciar el juego.
        self.apuesta=apuesta
        self.puntos=self.carta[0]+self.carta[1]


    def pedir(self):
        if self.puntos<21:
            pedir=random.randint(1, 13)
            self.puntos=self.puntos+pedir
            self.carta.append(pedir)

lucero=player("Lucero",1000,500)


##print lucero.cartas
##lucero.pedir()

print lucero.cartas
print lucero.puntos
lucero.pedir()
print lucero.puntos









        


        
        
        
        
