#Author

from Jugador import Jugador

class Mago (Jugador):
    def __init__(self, nombre, arma, velocidad, resistencia, ataque):
        super().__init__(nombre)
        self.__armaM = arma
        self.__velocidadM = velocidad
        self.__resistenciaM = resistenca
        self.__ataqueM = ataque

    def setArma (self, arma):
        self.__armaM = arma

    def getArma (self):
        return self.__armaM

    def setVelocidad (self, velocidad):
        self.__VelocidadM = velocidad

    def getVelocidad (self):
        return self.__VelocidadM
    
    def setResistencia (self, resistencia):
        self.__ResistenciaM = resistencia

    def getResistencia (self):
        return self.__ResistenciaM

    def setAtaque (self, ataque):
        self.__AtaqueM = ataque

    def getAtaque (self):
        return self.__AtaqueM
