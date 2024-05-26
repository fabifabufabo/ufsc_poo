from pessoa import Pessoa


class Tecnico(Pessoa):
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome
