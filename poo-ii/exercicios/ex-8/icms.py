from imposto import Imposto

'''
O calculo da Aliquota do ICMS (percentual do imposto)
leva em conta a "diferenca_estado".
O valor de "diferenca_estado" deve ser somado a aliquota informada.
Por exemplo, se a aliquota informada no construtor for 10.0
e a "diferenca_estado" for 2, entao a aliquota calculada sera de 12.0
'''


class ICMS(Imposto):
    def __init__(self, aliquota, diferenca_estado: float):
        super().__init__(aliquota)
        self.__diferenca_estado = diferenca_estado

    @property
    def diferenca_estado(self):
        return self.__diferenca_estado

    @diferenca_estado.setter
    def diferenca_estado(self, diferenca_estado):
        self.__diferenca_estado = diferenca_estado

    def calcula_aliquota(self) -> float:
        aliquota_icms = self.aliquota + self.__diferenca_estado
        return aliquota_icms
