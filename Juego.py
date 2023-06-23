#Author rrojano
# interfaz principal del juego

from Arquero import Arquero
from Mago import Mago
from Asesino import Assasin
import random
import sys

class Juego:
    def __init__(self):
        self.__monsters = {
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
        return self.__monsters

    def get_monsterNames(self): 
        return self.__monsters.keys()

    def get_monsterPower(self):
        return self.__monsters.values()

    def get_player(self):
        return self.__player
    
    def get_playerEnergia(self):
        return self.__player.get_energia()

    def get_playerEstadisticas(self):
        self.__player.estadisticas()

    def crearPlayer(self, n, c):
        print(chr(27)+"[37;44m")
        if c == "1":
            self.__player = Arquero(n)
            print(self.__player.nombreX,'aquí tienes tus estadísticas iniciales:')
            print(self.__player.estadisticas())
        if c == "2":
            self.__player = Assasin(n)
            print(self.__player.nombreX,'aquí tienes tus estadísticas iniciales:')
            print(self.__player.estadisticas())
        if c == "3":
            self.__player = Mago(n)
            print(self.__player.nombreX,'aquí tienes tus estadísticas iniciales:')
            prin(self.__player.estadisticas())
        print(chr(27)+"[0;30;0m")


    def validarEnergia(self):
        e = self.__player.get_energia()
        if e <= 2:
            print(chr(27)+"[37;41m")
            print('Estas a punto de morir, tu energia es:', e)
            print(chr(27)+"[0;30;0m")
        if e <1:
            print(chr(27)+"[37;41m")
            print('estás muerto!')
            print(chr(27)+"[0;30;0m")
            sys.exit() 

    def validarVida(self):
        v = self.__player.get_vida()
        ### print ( v )
        if v <= 2:
            print(chr(27)+"[37;41m")
            print('Estas a punto de morir, tu vida es:', v)
            print(chr(27)+"[0;30;0m")
        if v < 1:
            print(chr(27)+"[37;41m")
            print('estás muerto!')
            print(chr(27)+"[0;30;0m")
            sys.exit() 

    def downPowerMonster(self, monstruo):
        # básicamente es cosa de suerte el vencer tras un ataque, todo depende de las estadísticas 
        # y números aleatorios generados
        self.__monsters[monstruo] = random.randint (1, self.__player.get_resistencia())
        # cuando el power del monstruo acabe lo vencemos, si no nos quedamos sin vida
        ### print ('pw: ', self.__monsters[monstruo])
        #print ('pw:', self.__monsters[monstruo], 'vd:', self.__player.get_vida())
        print ('pw: {:3d} - vd: {:3d}'. format(self.__monsters[monstruo], (self.__player.get_vida())))
        if self.__monsters[monstruo] <= 0:
            print ('Bien, venciste')
            return None
        self.validarVida()



if __name__ == '__main__':
    c = ['Arquero', 'Asesino', 'Mago']
    print ('¿cuál es tu nombre?')
    nombrePy = input()
    print (nombrePy,'¿Escoge el número de tu clase?')
    print ('(1) Arquero  (2) Asesino  (3) Mago')
    clasePy = input()
    print('ok', chr(27)+"[1;33m"+nombrePy, 'tu clase es:', c[int(clasePy)-1])
    #print(chr(27)+"[0;30;0m")

    # inicializamos el juego
    jj = Juego()
    jj.crearPlayer(nombrePy, clasePy)
    monstruos = jj.get_monsters()
    for m in monstruos:
        print ('Te ataca ', m)
        print ('¿qué harás? (1) atacar (2) defender (3) ver estadísticas y huir')
        accion = input()
        if accion == '1':
            jj.get_player().atacar()
            jj.validarEnergia()
        if accion == '2':
            # básicamente si nos defendemos tendremos que aguantar 
            # hasta que el monstruo pierda power o nos quedemos sin vida :-D
            for x in range(monstruos[m]):
                ### print ('int' ,monstruos[m])
                jj.get_player().defender()
                jj.downPowerMonster(m)
        if accion == '3':
            jj.get_playerEstadisticas()
    print('Felicidades milagrosamente terminaste el ciclo for')       


