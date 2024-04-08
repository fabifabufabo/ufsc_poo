

class Cliente:

    def __init__ (self, nome, fone):
        self.__nome = nome
        self.__fone = fone


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self, value):
        self.__fone = value
