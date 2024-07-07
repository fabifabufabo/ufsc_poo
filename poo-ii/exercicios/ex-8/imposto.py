from abc import ABC, abstractmethod


class Imposto(ABC):
    def __init__(self, aliquota):
        self.__aliquota = aliquota

    @property
    def aliquota(self):
        return self.__aliquota

    '''
    Operacao abstrata que ira calcular a aliquota
    Cada classe que ira estender Imposto devera implementar o calculo de acordo
    com a sua regra
    '''

    @abstractmethod
    def calcula_aliquota(self) -> float:
        pass
