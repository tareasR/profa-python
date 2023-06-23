# interfaz principal del juego

from Arquero import Arquero
from Mago import Mago
# from Asesino import Assasin
import random

class Juego:
    def __init__(self):
        self.__monster = {
            "Dracón" : random.randint(40, 50), 
            "Basilisco" : random.randint(20, 30), 
            "Quimera" : random.randint(30, 45), 
            "Gorgona" : random.randint(9, 23), 
            "Kraken" : random.randint(30, 50), 
            "Espectro" : random.randint(10, 20), 
            "Orco" : random.randint(10, 50), 
            "Minotauro" : random.randint(10, 30), 
            "Hidra" : random.randint(10, 50), 
            "Ciclope" : random.randint(12, 30), 
            "Harpía" : random.randint(1, 5), 
            "Hombre lobo" : random.randint(5, 10), 
            "Vampiro" : random.randint(10, 30), 
            "Yeti" : random.randint(10, 50), 
            "Wendigo" : random.randint(12, 20), 
            "Fantasma" : random.randint(0, 20), 
            "Demonio" : random.randint(5, 12), 
            "Medusa" : random.randint(5, 15), 
            "Esqueleto" : random.randint(10, 15), 
            "Troll" : random.randint(4, 8)
        }
        self.__player = None

    def get_monsters(self):
        return self.__monster

    def get_monsterNames(self):
        return self.__monster.keys()

    def get_monsterPower(self):
        return self.__monster.values()

    def get_player(self):
        return self.__player

    def crearPlayer(self, n, c):
        if c == "1":
            self.__player = Arquero(n)
            print()
            print(self.__player.nombreX,'aquí tienes tus estadísticas iniciales:')
            print(self.__player.estadisticas())
        if c == "2":
            self.__player = Asesino(n)
            print()
            print(self.__player.nombreX,'aquí tienes tus estadísticas iniciales:')
            print(self.__player.estadisticas())
        if c == "3":
            self.__player = Mago(n)
            print()
            print(self.__player.nombreX,'aquí tienes tus estadísticas iniciales:')
            print(self.__player.estadisticas())


if __name__ == '__main__':
    jj = Juego()
    # jj.crearPlayer('rafa','1')
    # print (jj.get_player())

    c = ['Arquero', 'Asesino', 'Mago']
    print ('¿cuál es tu nombre?')
    nombrePy = input()
    print (nombrePy,'¿Escoge el número de tu clase?')
    print ('(1) Arquero  (2) Asesino  (3) Mago')
    clasePy = input()
    print('ok', nombrePy, 'tu clase es:', c[int(clasePy)-1])

    jj.crearPlayer(nombrePy, clasePy)
    #print (type(jj.get_player()).__name__)
    for monstruo in jj.get_monsters():
        print (monstruo)


