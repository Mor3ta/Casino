import random


class Game():
    mazo = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    puntos_Crupier=0
    catas_crupier=0


    def __init__(self,nombre,dinero):
        self.nombre= nombre
        self.mano=[]
        self.dinero=dinero
        self.apuesta=0
        self.puntos=0
         
 
    def apostar(self):
        self.apuesta=int(input("diga el monto de su apuesta"))
        if self.apuesta > self.dinero:
            print("El dinero no es suficiente para esta apuesta.")
            if self.dinero >0:
                print("Tu cantidad de dinero es {}".format(self.dinero))
                self.apuesta= int(input(" Apuesta otra cantidad"))
            else:
                if self.dinero<=0:
                    dinero=input("Deseas agregar dinero")
                    if dinero=="si":
                        self.dinero=int(input("cuanto deseas Agregar"))
                        self.apostar()
                    else:
                        print ("Termino el juego")
        else:                                                         
            self.mano= random.sample(self.mazo,  2)
            self.cartas_crupier=random.sample(self.mazo,  1)     
            self.puntos = sum(self.mano)
            print ("Cartas de {} {}".format(self.nombre,self.mano))
            print ("Cartas del crupier{}".format(self.cartas_crupier))
            print("Puntos de {} {}".format(self.nombre, self.puntos))
            self.pedir()


           
    def pedir(self):
        while self.puntos<21:
            nuevaCarta=input("Deseas otra carta")
            if nuevaCarta== "si":
                pedir=random.randint(1,13)
                self.mano.append(pedir)
                self.puntos=self.puntos+pedir
                print("{} pidio una carta {}".format(self.nombre,self.mano))
                print("Nueva puntuacion de {}:{}".format(self.nombre, self.puntos))
            else:
                if nuevaCarta=="no":
                    self.terminar()                   
        else:
            if len(self.mano)==2 and self.puntos==21:
                self.blackjack()
            if self.puntos >21:
                self.terminar()
                
         

 
   
    def duplicar(self):
        self.apuesta= self.apuesta *2
        self.dinero= self.dinero-self.apuesta
        self.pedir()
        self.terminar()


    def blackjack(self):
        if self.puntos ==21:
            self.apuesta= self.apuesta*2
            print ("{}BLACKJACK! You win ${}".format(self.nombre,self.apuesta))

    def terminar(self):

        if self.puntos > 21:
            self.dinero = self.dinero - self.apuesta
            print("${}: LOSE  Tu cantidad de Dinero actual es ${}".format(self.nombre, self.dinero))
        else:
            print("{} termino la partida, el Crupier inicia a jugar.".format(self.nombre))
            revelar = random.randint(1, 13)
            self.cartas_crupier.append(revelar)       
            self.puntos_crupier = sum(self.cartas_crupier)
            while self.puntos_crupier < 17:
                self.cartas_crupier.append(revelar)
                self.puntos_crupier= sum(self.cartas_crupier) 
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



   
        
    


player=input("cual es tu nombre?")
dinero=int(input("cual es tu monto disponible para jugar?"))
if dinero<=0:
    dinero= int(input("Introdusca un monto valido para apostar"))
player=Game(player, dinero)
player.apostar()
    









        



   









