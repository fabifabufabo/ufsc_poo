from abc import ABC, abstractmethod

from onibusJahCheioException import OnibusJahCheioException
from onibusJahDesligadoException import OnibusJahDesligadoException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahVazioException import OnibusJahVazioException


class AbstractOnibus(ABC):
    @abstractmethod
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        pass

    # OnibusJahLigadoException
    @abstractmethod
    def ligar(self) -> str:
        pass

    # OnibusJahDesligadoException
    @abstractmethod
    def desligar(self) -> str:
        pass

    # OnibusJahCheioException
    @abstractmethod
    def embarca_pessoa(self) -> str:
        pass

    # OnibusJahVazioException
    @abstractmethod
    def desembarca_pessoa(self) -> str:
        pass

    @property
    @abstractmethod
    def capacidade(self) -> int:
        pass

    @property
    @abstractmethod
    def total_passageiros(self) -> int:
        pass

    @property
    @abstractmethod
    def ligado(self) -> bool:
        pass

    @capacidade.setter
    @abstractmethod
    def capacidade(self, capacidade: int):
        pass


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        self.__capacidade = capacidade
        self.__total_passageiros = total_passageiros
        self.__ligado = ligado

    """Setters e Getters"""

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def total_passageiros(self) -> int:
        return self.__total_passageiros

    @property
    def ligado(self) -> bool:
        return self.__ligado

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    """Metodos"""

    def ligar(self) -> str:
        if self.__ligado:
            raise OnibusJahLigadoException()
        self.__ligado = True
        return "Onibus ligado"

    def desligar(self) -> str:
        if not self.__ligado:
            raise OnibusJahDesligadoException()
        self.__ligado = False
        return "Onibus desligado"

    def embarca_pessoa(self) -> str:
        if self.__total_passageiros == self.__capacidade:
            raise OnibusJahCheioException()
        self.__total_passageiros += 1
        return "Passageiro entrou no onibus"

    def desembarca_pessoa(self) -> str:
        if self.__total_passageiros == 0:
            raise OnibusJahVazioException()
        self.__total_passageiros -= 1
        return "Passageiro saiu do onibus"
