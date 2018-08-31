import random

class Game():
    puntos=0
    def __init__(self,nombre,dinero):
        self.nombre= nombre
        self.mano=[]
        self.dinero=dinero  # cantidad de dinero al iniciar el juego.
        self.apuesta=0
        self.puntos=0
        
 
    def apostar(self,apostar):
        self.apuesta=apostar
        mazo=[1, 2, 3, 4, 5,6,7,8,9,10,11,12,13]                   # Accion del jugador, Recibe el monto que el jugador decea apostar
                                                                   # y devuelve dos cartas y la cantidad de punto de este. 
        self.mano= random.sample(mazo,  2)
        print self.mano
        self.puntos=self.mano[0]+self.mano[1]
        print self. puntos
   
           
    def pedir(self):
        if self.puntos<21:
            pedir=random.randint(1, 13)
            self.mano.append(pedir)                                #Agrega una carta al jugador, suma los puntos. 
            self.puntos=self.puntos+pedir
            print self.mano
            print self.puntos
     
   
    def duplicar(self):
        self.apuesta= self.apuesta *2
        self.dinero= self.dinero-self.apuesta
        self.pedir()                                                #Dobla la apuesta iniciar y agregar una carta a la mano.
                                                                    #El jugador ya no puede pedir mas cartas.
        
   
    def repartir (self) :
        mazo=[1, 2, 3, 4, 5,6,7,8,9,10,11,12,13]
        self.mano= random.sample(mazo,  1)                           #OJO: choca con el metodo apostar, hacer que este metodo sea llamado
                                                                     #por apostar
                                                                     #reparte las cartas de la mesa 
        
   
    def revelar (self):
        carta=random.randint(1, 13)
        self.mano.append(carta)                                     #Es llmado por el metodo STAND (cuando el jugador decide detener su mano) 



   
    def pagar(self):                                              # Si el jugador gana la mesa duplica el monto que aposto, si este pierde resta el
                                                                  #monto de la apuesta al dinero del jugador.




#NOTAS:
#AGREGAR  CARTAS A,J,Q,K.


        


   








