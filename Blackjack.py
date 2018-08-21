import random

class Crupier():
    
    def __init__(self):
        self.mano=[]

    def repartir (self) :
        mazo=[1, 2, 3, 4, 5,6,7,8,9,10,11,12,13]
        Player.mano=random.sample(mazo,  2)
        self.mano= random.sample(mazo,  1)
    def revelar (self):
        carta=random.randint(1, 13)
        self.mano.append(carta)

    def pedir(self):
        if self.puntos<21:
            pedir=random.randint(1, 13)
            self.mano.append(pedir)
            self.puntos=self.puntos+pedir
            print self.mano
            print self.puntos    

class Player():
    puntos=0
    def __init__(self,nombre,dinero,apuesta):
        self.nombre= nombre
        self.mano=[]
        self.dinero=dinero  # cantidad de dinero al iniciar el juego.
        self.apuesta=apuesta
        self.puntos=self.puntos
        
            
    def duplicar(self):
        self.apuesta= self.apuesta *2
        self.dinero= self.dinero-self.apuesta
        self.pedir()



        






        


   








