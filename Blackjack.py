import random

class  player():
    mano=[]
    puntos=0
    def __init__(self,nombre,dinero,apuesta):
        self.nombre= nombre
        self.mano=self.mano
        self.dinero=dinero  # cantidad de dinero al iniciar el juego.
        self.apuesta=apuesta
        self.puntos=self.puntos
        
    def play(self):
        pick=random.sample([1, 2, 3, 4, 5,6,7,8,9,10,11,12,13],  2)
        self.mano=pick
        puntos=pick[0]+pick[1]
        self.puntos=puntos
        print self.mano
        print self.puntos


    def pedir(self):
        if self.puntos<21:
            pedir=random.randint(1, 13)
            self.mano.append(pedir)
            self.puntos=self.puntos+pedir
            print self.mano
            print self.puntos
            
    def duplicar(self):
        self.apuesta= self.apuesta *2
        self.dinero= self.dinero-self.apuesta
        self.pedir()

lucero=player("Lucero",5000,1500)

lucero.play()
lucero.duplicar()
print lucero.mano







