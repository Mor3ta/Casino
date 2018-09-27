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

    def repatirCartas(self):
        self.mano = random.sample(self.mazo, 2)
        self.cartas_crupier = random.sample(self.mazo, 1)
        self.puntos = sum(self.mano)
        print("\t CARTAS DE{} {}.  ".format(self.nombre, self.mano))
        print("\t PUNTOS DE {} {} ".format(self.nombre, self.puntos))
        print("\t CARTAS DEL CRUPIER {}".format(self.cartas_crupier))

 #Cambio en apostar!
    def apostar(self):
        self.apuesta=int(input("DIGA EL MONTO QUE DESEA APOSTAR  "))
        while self.apuesta > self.dinero:
            self.apuesta=int(input(("EL DINERO NO ES SUFICIENTE PARA REALIZAR ESTA APUESTA. DIGITE OTRA CANTIDAD? ")))
        self.repatirCartas()
        self.pedir()

    def pedir(self):
        while self.puntos<21:
            nuevaCarta=input("DESEAS OTRA CARTA  ")
            if nuevaCarta.lower()== "si":
                pedir=random.randint(1,13)
                self.mano.append(pedir)
                self.puntos=self.puntos+pedir
                print("\t {} PIDIO UNA CARTA \n \t MANO DE {} TU NUEVA PUNTUACION ES {}\n".format(self.nombre,self.mano,self.puntos))
            else:
                if nuevaCarta.lower()=="no":
                    self.terminar()
        if len(self.mano)==2 and self.puntos==21:
            self.blackjack()
        if self.puntos >=21:
            self.terminar()

    def blackjack(self):
        if self.puntos ==21:
            self.apuesta= self.apuesta*2
            print ("{}BLACKJACK! YOU WIN ${}".format(self.nombre,self.apuesta))

    def terminar(self):

        if self.puntos > 21:
            self.dinero = self.dinero - self.apuesta
            print("${}: LOSE  Tu cantidad de Dinero actual es ${}".format(self.nombre, self.dinero))
        else:
            print(" TERMINO EL TURNO DE {}.\n TURNO DEL CRUPIER.\n".format(self.nombre))
            revelar = random.randint(1, 13)
            self.cartas_crupier.append(revelar)       
            self.puntos_crupier = sum(self.cartas_crupier)
            while self.puntos_crupier < 17:
                self.cartas_crupier.append(revelar)
                self.puntos_crupier= sum(self.cartas_crupier) 
            print("MANO DEL CRUPIER:{}. PUNTOS {}".format(self.cartas_crupier,self.puntos_crupier))

            #RESULTADOS
            if self.puntos_crupier >21:
                self.dinero = self.dinero + self.apuesta*2
                print ("{}: WIN ${} Tu cantidad de Dinero actual es ${}".format(self.nombre,self.apuesta,self.dinero))
            if self.puntos_crupier == self.puntos:
                print ("EMPATADOS")
            if self.puntos_crupier > self.puntos and self.puntos_crupier <= 21:
                self.dinero=self.dinero-self.apuesta
                print("Crupier WIN. Tu cantidad de Dinero es ${}".format(self.dinero))
            if self.puntos > self.puntos_crupier:
                self.dinero=self.dinero+self.apuesta*2
                print("{} WIN. Tu cantidad de Dinero es ${}".format(self.nombre,self.dinero))
        #NUEVA PARTIDA        
        nuevoJuego=input("DECEAS VOLVER A JUGAR  ")
        if nuevoJuego.lower()=="si"and player.dinero>0:
            player.apostar()
        else:
            if player.dinero<=0:
                nuevoMonto=(input("DESEAS AGREGAR UNA NUEVA CANTIDAD DE DINERO"))
                if nuevoMonto.lower()== "si":
                    player.dinero= int (input("DIGITA LA NUEVA CANTIDAD DE DINERO  "))
                    player.apostar()
                else:
                    print ("LA PARTIDA TERMINO")
            if nuevoJuego.lower()=="no":
                print ("EL JUEGO TERMINO!")
      


print ("REGLAS:  | CONTESTA SI O NO A LAS PREGUNTAS. | |COLOCA LOS MONTOS SIN SIGNOS NI PUNTOS. |\n")
player=input("CUAL ES TU NOMBRE?")
dinero=int(input("CON QUE CANTIDAD DE DINERO QUIERES JUGAR"))
if dinero<=0:
    dinero= int(input("INTRODUSCA UN MONTO VALIDO PARA APOSTAR"))
player=Game(player, dinero)
player.apostar()


                
    









        



   









