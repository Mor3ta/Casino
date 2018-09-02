import random

class Game():

    def __init__(self,nombre,dinero):
        self.nombre= nombre
        self.mano=[]
        self.dinero=dinero  # cantidad de dinero al iniciar el juego.
        self.apuesta=0
        self.puntos=0
        self.puntos_crupier=0
        self.cartas_crupier=[]

        
 # Accion del jugador, Recibe el monto que el jugador decea apostar
 # y devuelve dos cartas y la cantidad de punto de este.
 
    def apostar(self,apostar):
        mazo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.apuesta=apostar
        self.mano= random.sample(mazo,  2)
        self.cartas_crupier=random.sample(mazo,  1)
        print (self.mano)
        for i in self.mano:
            self.puntos=self.puntos +i
        print (self.puntos)
        print (self.cartas_crupier)


    # Agrega una carta al jugador, suma los puntos.
           
    def pedir(self):
        if self.puntos<21:
            pedir=random.randint(1, 13)
            self.mano.append(pedir)
            self.puntos=self.puntos+pedir
            print (self.mano)
            print (self.puntos)


    # Dobla la apuesta iniciar y agregar una carta a la mano.
    # El jugador ya no puede pedir mas cartas.
   
    def duplicar(self):
        self.apuesta= self.apuesta *2
        self.dinero= self.dinero-self.apuesta
        self.pedir() 

    def terminar(self):
        pedir = random.randint(1, 13)
        self.cartas_crupier.append(pedir)
        for i in self.cartas_crupier:
            self.puntos_crupier = self.puntos_crupier + i
        print(self.puntos_crupier)
        print (self.cartas_crupier)
        if self.puntos > self.puntos_crupier:
            print ("Player win")
        else:
            self.dinero = self.dinero - self.apuesta
            print ("Player Lose ")






Lucero=Game("Lucero", 5000)
Lucero.apostar(500)
Lucero.pedir()
Lucero.terminar()
print(Lucero.dinero)



#NOTAS:
#AGREGAR  CARTAS A,J,Q,K.


        



   








