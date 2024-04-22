from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            for l in self.__livros:
                if l.titulo == livro.titulo:
                    return
            self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            for l in self.__livros:
                if l.titulo == livro.titulo:
                    self.__livros.remove(l)
                    return 

    @property
    def livros(self):
        return self.__livros
