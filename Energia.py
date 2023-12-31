#Author rrojano

import random
class Energia:
    __energia = random.randint(10, 50)
    __vida = 100

    def get_energia(self):
        return self.__energia

    # de acuerdo con la clase que ejecute el ataque se generará un gasto de energía aleatorio
    def set_energia(self):
        if type(self).__name__ == 'Arquero':
            self.__energia = self.__energia - random.randint(3, 5)
        if type(self).__name__ == 'Mago':
            self.__energia = self.__energia - random.randint(1, 3)
        if type(self).__name__ == 'Assasin':
            self.__energia = self.__energia - random.randint(2, 6)        

    def get_vida(self):
        return self.__vida

    # básicamente si nos defendemos también perdemos vida de forma aleatoria
    def set_vida(self):
        if type(self).__name__ == 'Arquero':
            self.__vida = self.__vida - random.randint(3, 5)
        if type(self).__name__ == 'Mago':
            self.__vida = self.__vida - random.randint(1, 3)
        if type(self).__name__ == 'Assasin':
            self.__vida = self.__vida - random.randint(2, 6)     