from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return self.__clientes

    @property
    def tecnicos(self):
        return self.__tecnicos

    def inclui_cliente(self, codigo, nome):
        existe = False
        for cliente in self.clientes:
            if cliente.codigo == codigo:
                existe = True
                break
        if not existe:
            cliente = Cliente(nome, codigo)
            self.clientes.append(cliente)
            return cliente

    def inclui_tecnico(self, codigo, nome):
        existe = False
        for tecnico in self.tecnicos:
            if tecnico.codigo == codigo:
                existe = True
                break
        if not existe:
            tecnico = Tecnico(nome, codigo)
            self.tecnicos.append(tecnico)
            return tecnico
