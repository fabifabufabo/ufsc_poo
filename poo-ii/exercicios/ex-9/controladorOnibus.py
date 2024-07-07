from abc import ABC, abstractmethod

from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class AbstractControladorOnibus(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def ligar(self) -> str:
        pass

    @abstractmethod
    def desligar(self) -> str:
        pass

    @abstractmethod
    def embarca_pessoa(self) -> str:
        pass

    @abstractmethod
    def desembarca_pessoa(self) -> str:
        pass

    @property
    @abstractmethod
    def onibus(self) -> Onibus:
        pass

    @abstractmethod
    def inicializar_onibus(self, capacidade: int, total_passageiros: int,
                           ligado: bool):
        pass


class ControladorOnibus(AbstractControladorOnibus):

    def __init__(self):
        self.__onibus = None

    def ligar(self) -> str:
        return self.__onibus.ligar()

    def desligar(self) -> str:
        return self.__onibus.desligar()

    def embarca_pessoa(self) -> str:
        return self.__onibus.embarca_pessoa()

    def desembarca_pessoa(self) -> str:
        return self.__onibus.desembarca_pessoa()

    @property
    def onibus(self) -> Onibus:
        return self.__onibus

    def inicializar_onibus(self, capacidade: int, total_passageiros: int,
                           ligado: bool):
        if (
                not all(isinstance(x, int) for x in
                        [capacidade, total_passageiros])
                or not isinstance(ligado, bool)
                or any(x < 0 for x in [capacidade, total_passageiros])
                or total_passageiros > capacidade
                or not ligado
        ):
            raise ComandoInvalidoException

        self.__onibus = Onibus(capacidade, total_passageiros, ligado)
