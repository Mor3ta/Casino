import random

class Game():
    mazo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    puntos_Crupier=0
    catas_crupier=0

    def __init__(self,nombre,dinero):
        self.nombre= nombre
        self.mano=[]
        self.dinero=dinero
        self.apuesta=0
        self.puntos=0


        
           # Accion del jugador, Recibe el monto que el jugador decea apostar
           # y devuelve dos cartas y la cantidad de punto de este. Y la carta inicial de Crupier.
 
    def apostar(self,apostar):
        self.apuesta=apostar
        if self.apuesta > self.dinero:
            print("El dinero no es suficiente para esta apuesta.")    # Muestra si el dinero que tienes es suficiente
        else:                                                         #Para la apuesta que quieres realizar.
            self.mano= random.sample(self.mazo,  2)
            self.cartas_crupier=random.sample(self.mazo,  1)      #Agrega de manera random una carta al Crupier y Dos al jugador.
            self.puntos = sum(self.mano)
            print ("Cartas de {} {}".format(self.nombre,self.mano))
            print ("Cartas del crupier{}".format(self.cartas_crupier))
            print("Puntos de {} {}".format(self.nombre, self.puntos))


    # Agrega una carta al jugador, suma los puntos.
           
    def pedir(self):
        if self.puntos<21:
            pedir=random.randint(1,13)
            self.mano.append(pedir)
            self.puntos=self.puntos+pedir
            print("{} pidio una carta {}".format(self.nombre,self.mano))
            print("Nueva puntuacion de {}:{}".format(self.nombre, self.puntos))


    # Dobla la apuesta iniciar y agregar una carta a la mano.
    # El jugador ya no puede pedir mas cartas.
   
    def duplicar(self):
        self.apuesta= self.apuesta *2
        self.dinero= self.dinero-self.apuesta
        self.pedir()
        self.terminar()

    #Finaliza el turno del jugador e inicia el turno del Crupier.
    #Devuelve quien es el ganador del juego.

    def terminar(self):
        print("{} termino la partida, el Crupier inicia a jugar." .format(self.nombre))
        revelar = random.randint(1, 13)
        self.cartas_crupier.append(revelar)       #Muestra la carta oculta del crupier
        self.puntos_crupier = sum(self.cartas_crupier)
        while self.puntos_crupier < 17:
            self.cartas_crupier.append(revelar)
            self.puntos_crupier= sum(self.cartas_crupier) #Pide Cartas al Crupier hasta que este llega a una puntuacion de 17
        print("Cartas del Crupier:{}".format(self.cartas_crupier))
        print ("Puntos del Curpier:{}".format(self.puntos_crupier))

        #RESULTADO
        # if self.puntos > self.puntos_crupier:
        #     self.dinero = self.dinero+self.apuesta *2
        #     print ("${}: WIN  Tu cantidad de Dinero actual es ${}".format(self.nombre,self.dinero))
        #
        # else:
        #     self.dinero = self.dinero - self.apuesta
        #     print ("{}: Lose ${} Tu cantidad de Dinero actual es ${}".format(self.nombre,self.apuesta,self.dinero))






Lucero=Game("Lucero", 5000)
Lucero.apostar(1000)
Lucero.pedir()
Lucero.terminar()
print(Lucero.dinero)






        



   








