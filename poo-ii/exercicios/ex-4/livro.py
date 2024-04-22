from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        # Criar todos os atributos, incluindo as listas
        # Incluir o primeiro autor e o primeiro capitulo nas respectivas listas
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]
        

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            autor_existe = False
            for a in self.__autores:
                if a.nome == autor.nome:
                    autor_existe = True
                    break
            if not autor_existe:
                self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            for a in self.__autores:
                if a.nome == autor.nome:
                    self.__autores.remove(a)

    def incluir_capitulo(self, numero: int, titulo: str):
        capitulo_existe = False
        for capitulo in self.__capitulos:
            if capitulo.numero == numero and capitulo.titulo == titulo:
                capitulo_existe = True
                break
        if not capitulo_existe:
            self.__capitulos.append(Capitulo(numero, titulo))

    def excluir_capitulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                self.__capitulos.remove(capitulo)

    def find_capitulo_by_titulo(self, titulo: str):
        # Procura na lista de capitulos se existe um Capitulo com este titulo 
        # Se encontrar, retorna o Capitulo encontrado
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
