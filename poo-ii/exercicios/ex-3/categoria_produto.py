

class CategoriaProduto:

    def __init__(self, titulo):
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, value):
        self.__titulo = value


