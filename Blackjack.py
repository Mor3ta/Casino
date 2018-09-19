import random

class Game():
    mazo = [1, 2, 3, 4,5,6,7,8,9,10,11,12,13]
    puntos_Crupier=0
    catas_crupier=0

    def __init__(self,nombre,dinero):
        self.nombre= nombre
        self.mano=[]
        self.dinero=dinero
        self.apuesta=0
        self.puntos=0
            #Inicia el juego
           # Accion del jugador, Recibe el monto que el jugador decea apostar
           # y devuelve dos cartas y la cantidad de punto de este. Y la carta inicial de Crupier.
 
    def apostar(self):
        self.apuesta=int(input("diga el monto de su apuesta"))
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
        else:
            if self.puntos == 21:
                self.blackjack()  # OJO: agregar impresion blackjac en el metodo terminar.

    # Dobla la apuesta y
    #iniciar y agregar una carta a la mano.
    # El jugador ya no puede pedir mas cartas.
   
    def duplicar(self):
        self.apuesta= self.apuesta *2
        self.dinero= self.dinero-self.apuesta
        self.pedir()
        self.terminar()

    #Finaliza el turno del jugador e inicia el turno del Crupier.
    #Devuelve quien es el ganador del juego.

    def blackjack(self):
        if self.puntos ==21:
            self.apuesta= self.apuesta*2
            print ("{}BLACKJACK! You win ${}").format(self.nombre,self.nombre)

    def terminar(self):

        if self.puntos > 21:
            self.dinero = self.dinero - self.apuesta
            print("${}: LOSE  Tu cantidad de Dinero actual es ${}".format(self.nombre, self.dinero))
        else:
            print("{} termino la partida, el Crupier inicia a jugar.".format(self.nombre))
            revelar = random.randint(1, 13)
            self.cartas_crupier.append(revelar)       #Muestra la carta oculta del crupier
            self.puntos_crupier = sum(self.cartas_crupier)
            while self.puntos_crupier < 17:
                self.cartas_crupier.append(revelar)
                self.puntos_crupier= sum(self.cartas_crupier) #Pide Cartas al Crupier hasta que este llega a una puntuacion de 17
            print("Cartas del Crupier:{}".format(self.cartas_crupier))
            print ("Puntos del Curpier:{}".format(self.puntos_crupier))

            #RESULTADOS
            if self.puntos_crupier >21:
                self.dinero = self.dinero + self.apuesta*2
                print ("{}: WIN ${} Tu cantidad de Dinero actual es ${}".format(self.nombre,self.apuesta,self.dinero))
            # El crupier empata con el jugador.

            if self.puntos_crupier == self.puntos:
                print ("EMPATADOS")
            #El crupier saca una puntuacion mayor que el jugador sin pasarse o El jugador saca una puntuacion mayor que
            #la del Crupier sin pasarse

            if self.puntos_crupier > self.puntos and self.puntos_crupier < 21:
                print("Crupier WIN")

            else:
                print("{}: WIN ${} Tu cantidad de Dinero actual es ${}".format(self.nombre, self.apuesta, self.dinero))




def play():
    player.apostar()
    while player.puntos <=21:
        pedir=input("deceas pedir una carta?")
        if pedir== "si":
            player.pedir()
        else:
            player.terminar()
            break
   
        
    






player=input("cual es tu nombre?")
dinero=int(input("cual es tu monto disponible para jugar?"))
player=Game(player, dinero)
play()
if player.dinero!=0:
    continuar=input("continuar jugando?")
    if continuar == "si":
        play()
    else:
        print ("La partida termino")
    









        



   









