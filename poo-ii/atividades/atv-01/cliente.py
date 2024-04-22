

class Cliente:

    def __init__(self, nome, fone, email):
        self.nome = nome
        self.fone = fone
        self.email = email

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_fone(self):
        return self.__fone

    def set_fone(self, fone):
        self.__fone = fone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

