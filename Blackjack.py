import random

class  player():
    mano=[]
    def __init__(self,nombre,dinero,apuesta):
        self.nombre= nombre
        self.mano=self.mano
        self.dinero=dinero  # cantidad de dinero al iniciar el juego.
        self.apuesta=apuesta
        #self.puntos=self.mano[0]+self.mano[1]
        
    def play(self):
        pick=random.sample([1, 2, 3, 4, 5,6,7,8,9,10,11,12,13],  2)
        self.mano=pick
        print self.mano
         
    


    def pedir(self):
        if self.puntos<21:
            pedir=random.randint(1, 13)
            self.carta.append(pedir)
            self.puntos=self.puntos+pedir
            print self.cartas
            print self.puntos

lucero=player("Lucero",1000,500)
lucero.play()
#lucero.pedir()






