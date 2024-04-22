

from cliente import Cliente
from pacote_viagem import PacoteViagem



class Venda:

    def __init__(self, codigo, cliente, descricao, origem, destino, duracao, custo_unitario):
    
        self.__codigo = codigo
        self.__cliente = cliente
        self.__descricao = descricao
        self.__pacote = PacoteViagem(origem, destino, duracao, custo_unitario)
        self.__quantidade = None

    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_cliente(self):
        return self.__cliente
    
    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_pacote(self):
        return self.__pacote
    
    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    def preco_total(self):
        ...