from categoria_produto import CategoriaProduto
from cliente import Cliente

class Produto:

    def __init__ (self, codigo, descricao, categoria):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = CategoriaProduto(categoria)
        self.__quantidade = None
        self.__preco_unitario = None
        self.__cliente = Cliente(None, None)

    # Properties and setters
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        self.__codigo = value

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, value):
        self.__categoria = value

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, value):
        self.__quantidade = value

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, value):
        self.__preco_unitario = value

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, value):
        self.__cliente = value

    # Function that calculates the price
    def preco_total(self):
        total = float()
        total = self.__quantidade * self.__preco_unitario
        return total




    