#Author Pablo

  from Jugador import Jugador
    from Energia import Energia
    
    class Assasin(Jugador, Energia):
        
        def __init__(self, nombre):
            super().__init__(nombre)
            self.arma = 'pistola'
            self.velocidad = 80
            self.resistencia = 50
            self.ataque = 70
            
        def clase(self):
            print ('Clase' , type(self), self.nombreX)

        def estadistica(self):
            print('velocidad: ', self.velocidad)
            print('resistencia: ', self.resistencia)
            print('ataque: ', self.ataque)
            print('vida: ', super().get_vida())
            print('energia: ', self.get_energia())

        
        def defender(self):
            super().set.vida()
        
        def atacar (self):
            super().set_energia()
            
        def get_resistencia(self):             
            return self.resitencia

      
            
