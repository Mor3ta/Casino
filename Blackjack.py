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
        self.apuesta=int(input("DIGA EL MONTO QUE DESEA APOSTAR \n "))
        if self.apuesta > self.dinero:
            print("EL DINERO NO ES SUFICIENTE PARA REALIZAR ESTA APUESTA.")
            if self.dinero >0:
                print(" TU CANTIDAD DE DINERO ES {}".format(self.dinero))
                self.apuesta= int(input(" APUESTA OTRA CANTIDAD"))
                if self.apuesta>self.dinero:
                    self.mano= random.sample(self.mazo,  2)
                    self.cartas_crupier=random.sample(self.mazo,  1)     
                    self.puntos = sum(self.mano)
                    print ("\t*(10) CARTAS DE{} {}.".format(self.nombre,self.mano))
                    print(" \t PUNTOS DE {} {} ".format(self.nombre, self.puntos))
                    print ("\t CARTAS DEL CRUPIER {}".format(self.cartas_crupier))
                    self.pedir()
                    
            else:
                if self.dinero<=0:
                    dinero=input("DESEAS AGREGAR MAS DINERO  ")
                    if dinero=="si":
                        self.dinero=int(input("CUANTO DINERO DESEAS AGREGAR  "))
                        self.apostar() 
                    else:
                        print ("TERMINO EL JUEGO")
        else:                                                         
          self.mano= random.sample(self.mazo,  2)
          self.cartas_crupier=random.sample(self.mazo,  1)     
          self.puntos = sum(self.mano)
          print ("\t  MANOS DE  {} {}.PUNTOS  {} ".format(self.nombre,self.mano,self.puntos))
          print ("\t  MANOS DEL CRUPIER {}".format(self.cartas_crupier))
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
                    break
        else:
            if len(self.mano)==2 and self.puntos==21:
                self.blackjack()
            if self.puntos >=21:
                self.terminar()
                                    
    
   
    def duplicar(self):
        self.apuesta= self.apuesta *2
        self.dinero= self.dinero-self.apuesta
        self.pedir()
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
                player.dinero=int(input("No tienes Dinero suficiente agrega mas dinero"))

            if nuevoJuego.lower()=="no":
                
                print ("EL JUEGO TERMINO!")
      


print ("REGLAS:  | CONTESTA SI O NO A LAS PREGUNTAS. | |COLOCA LOS MONTOS SIN SIGNOS NI PUNTOS. |\n")
player=input("CUAL ES TU NOMBRE?")
dinero=int(input("CON QUE CANTIDAD DE DINERO QUIERES JUGAR"))
if dinero<=0:
    dinero= int(input("INTRODUSCA UN MONTO VALIDO PARA APOSTAR"))
player=Game(player, dinero)
player.apostar()


                
    









        



   









