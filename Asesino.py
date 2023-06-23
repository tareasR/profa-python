#Author 
from Jugador import Jugador

class Assasin(Jugador):
    super(self)
    def __init__(self, nombre, arma, velocidad, resistencia, ataque):
        self.__nombreA = nombre
        self.__armaA = arma
        self.__velocidadA = velocidad
        self.__resistenciaA = resistencia
        self.__ataqueA = ataque

    def setArma (self, arma):
        self.__armaA = arma
    def get_Arma(self):             
        return self.__armaA

    def setVelocidad (self, velocidad):
        self.__velocidadA = velocidad
    def get_Velocidad(self):             
        return self.__velocidadA
    
    def setResistencia (self, resistencia):
        self.__resistenciaA = resistencia
    def get_Resistencia(self):             
        return self.__ResistenciaA
    
    def setAtaque (self, ataque):
        self.__ataqueA = ataque
    def get_Ataque(self):             
        return self.__ataqueA

      
            
