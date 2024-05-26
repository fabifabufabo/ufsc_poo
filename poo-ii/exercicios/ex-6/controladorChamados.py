from abstractControladorChamados import AbstractControladorChamados
from chamado import Chamado
from cliente import Cliente
from tecnico import Tecnico
from tipoChamado import TipoChamado
from datetime import date as Date


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    @property
    def chamados(self):
        return self.__chamados

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados

    def total_chamados_por_tipo(self, tipo):
        total = 0
        for chamado in self.chamados:
            if chamado.tipo == tipo:
                total += 1
        return total

    def checa_tipo_chamado(self, data: Date, cliente: Cliente,
                           tecnico: Tecnico,
                           titulo: str,
                           descricao: str, prioridade: int,
                           tipo: TipoChamado):

        return all((isinstance(data, Date), isinstance(cliente, Cliente),
                    isinstance(tecnico, Tecnico), isinstance(titulo, str),
                    isinstance(descricao, str),
                    isinstance(prioridade, int),
                    isinstance(tipo, TipoChamado)))

    def inclui_chamado(
            self, data: Date, cliente: Cliente, tecnico: Tecnico,
            titulo: str,
            descricao: str, prioridade: int,
            tipo: TipoChamado) -> Chamado | None:

        if self.checa_tipo_chamado(data, cliente, tecnico, titulo, descricao,
                                   prioridade, tipo):
            for chamado in self.chamados:
                if (
                        chamado.data == data
                        and chamado.cliente == cliente
                        and chamado.tecnico == tecnico
                        and chamado.tipo == tipo
                ):
                    return None
            chamado = Chamado(data, cliente, tecnico, titulo, descricao,
                              prioridade, tipo)
            self.chamados.append(chamado)
            return chamado

    def inclui_tipochamado(self, codigo, nome, descricao):
        existe = False
        for tipo_chamado in self.tipos_chamados:
            if tipo_chamado.codigo == codigo:
                existe = True
                break
        if not existe:
            tipo_chamado = TipoChamado(codigo, descricao, nome)
            self.tipos_chamados.append(tipo_chamado)
            return tipo_chamado
