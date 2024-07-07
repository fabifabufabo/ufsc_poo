from imposto import Imposto


'''
O calculo da Aliquota do IPI (percentual do imposto) leva em conta
se existe "aliquota_adicional".
Se existir aliquota_adicional, a aliquota e aumentada em 10%.
Por exemplo, se a aliquota informada no construtor for 10.0
e existe "aliquota_adicional", entao a aliquota calculada sera de 11.0.
'''


class IPI(Imposto):
    def __init__(self, aliquota: float, tem_aliquota_adicional: bool):
        super().__init__(aliquota)
        self.__tem_aliquota_adicional = tem_aliquota_adicional

    def calcula_aliquota(self) -> float:
        aliquota_ipi = 0.0
        if self.__tem_aliquota_adicional:
            aliquota_ipi = self.aliquota * 1.1
        return aliquota_ipi
