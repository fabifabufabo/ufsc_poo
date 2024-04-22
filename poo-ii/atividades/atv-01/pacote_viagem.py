

class PacoteViagem:

    def __init__ (self, origem, destino, duracao, custo_unitario):
        self.__origem = origem
        self.__destino = destino
        self.__duracao = duracao
        self.__custo_unitario = custo_unitario

    def get_origem(self):
        return self.__cliente    

    def set_origem(self, origem):
        self.__origem = origem
    
    def get_destino(self):
        return self.__cliente

    def set_destino(self, destino):
        self.__destino = destino    
    
    def get_duracao(self):
        return self.__cliente
    
    def set_origem(self, duracao):
        self.__duracao = duracao

    def get_custo_unitario(self):
        return self.__cliente 
    
    def set_custo_unitario(self, custo_unitario):
        self.__custo_unitario = custo_unitario