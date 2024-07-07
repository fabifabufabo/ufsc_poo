from imposto import Imposto
from icms import ICMS
from ipi import IPI
from iss import ISS
from irpj import IRPJ


class Empresa:
    def __init__(self, cnpj: int, nome_de_fantasia: str):
        self.__cnpj = cnpj
        self.__nome_de_fantasia = nome_de_fantasia
        self.__impostos = []
        self.__faturamento_servicos = 0.0
        self.__faturamento_producao = 0.0
        self.__faturamento_vendas = 0.0

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def nome_de_fantasia(self):
        return self.__nome_de_fantasia

    @nome_de_fantasia.setter
    def nome_de_fantasia(self, nome_de_fantasia: str):
        self.__nome_de_fantasia = nome_de_fantasia

    '''
    Retorna a lista de impostos da empresa
    @return Lista de impostos da empresa
    '''

    @property
    def impostos(self) -> list:
        return self.__impostos

    '''
    Inclui um imposto na lista de impostos da empresa
    A insercao so deve ser efetuada se o imposto
    ainda nao esta na lista e se ele nao eh nulo.
    Caso contrario, apenas nao incluir.
    @param imposto imposto a ser incluido
    '''

    def inclui_imposto(self, imposto: Imposto):
        if imposto not in self.impostos and imposto is not None:
            self.__impostos.append(imposto)

    '''
    Exclui um imposto cadastrado
    @param imposto a ser excluido da lista de impostos da empresa
    '''

    def remove_imposto(self, imposto: Imposto):
        self.__impostos.remove(imposto)

    @property
    def faturamento_servicos(self):
        return self.__faturamento_servicos

    @property
    def faturamento_producao(self):
        return self.__faturamento_producao

    @property
    def faturamento_vendas(self):
        return self.__faturamento_vendas

    '''
    Calcula o total dos faturamentos da empresa,
    somando: faturamento_producao,
        faturamento_servicos e faturamento_vendas
    @return Somatorio dos faturamentos
    '''

    def faturamento_total(self) -> float:
        return sum([self.faturamento_servicos, self.__faturamento_producao,
                    self.faturamento_vendas])

    '''
    Calcula o total de todos os impostos da empresa
    Percorre a lista de impostos da empresa,
    aplicando a aliquota de cada imposto.
    Leva em conta o tipo de cada imposto para aplicar
    a aliquota ao faturamento de Producao, Vendas,
        Servicos ou sobre o Total.
    O imposto IPI eh aplicado sobre o faturamento de producao,
    o imposto ICMS eh aplicado sobre o faturamento de vendas,
    o imposto ISS eh aplicado sobre o faturamento de servicos e
    o imposto IRPJ eh aplicato sobre o faturamento total.
    Nao esqueca que as aliquotas dos impostos estao em percentuais!
    @return valor total dos impostos da empresa
    '''

    def total_impostos(self) -> float:
        somatoria_total_impostos = 0.0
        for imposto in self.impostos:
            if isinstance(imposto, IPI):
                somatoria_total_impostos += self.faturamento_producao * (
                    imposto.calcula_aliquota() / 100)
            elif isinstance(imposto, ICMS):
                somatoria_total_impostos += self.faturamento_vendas * (
                    imposto.calcula_aliquota() / 100)
            elif isinstance(imposto, ISS):
                somatoria_total_impostos += self.faturamento_servicos * (
                    imposto.calcula_aliquota() / 100)
            elif isinstance(imposto, IRPJ):
                somatoria_total_impostos += self.faturamento_total() * (
                    imposto.calcula_aliquota() / 100)
        return somatoria_total_impostos

    def set_faturamentos(self,
                         fat_servicos: float,
                         fat_producao: float,
                         fat_vendas: float):
        self.__faturamento_servicos = fat_servicos
        self.__faturamento_producao = fat_producao
        self.__faturamento_vendas = fat_vendas
