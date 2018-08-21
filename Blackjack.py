import random

class Crupier():
    
    def __init__(self):
        self.mano=[]

    def repartir (self) :
        mazo=['As', '2', '3', '4', '5','6','7','8','9','10','j','Q','k']
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
        
    def play(self):
        pick=random.sample(['As', '2', '3', '4', '5','6','7','8','9','10','j','Q','k'],  2)
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



        


x= Crupier()
x.repartir()
print x.mano
x.revelar()
print x.mano




        


   








