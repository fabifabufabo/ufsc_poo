

#RS = float(input()) # Dinheiro Atual
#PE = float(input()) # Preço Envelope
#PS = float(input()) # Preço Selo
#QS = int(input()) # Qtd. Atual Selo
#QE = int(input()) # Qtd. Atual Envelope

RS = 20
PE = 1
PS = 0.5
QS = 4
QE = 2


class EnviaCarta:

    preco_envelope = None
    preco_selo = None 

    def __init__(self, RS, QS, QE):
        self.saldo = RS
        self.saldo_envelope = QE
        self.saldo_selo = QS

    def compra_produto(self, produto, qtd):
        if produto == "envelope":
            preco_compra = EnviaCarta.preco_envelope * qtd
            self.saldo_envelope += qtd
        
        elif produto == "carta":
            preco_compra = EnviaCarta.preco_selo * qtd
            self.saldo_selo += qtd
        
        else:
            preco_compra = EnviaCarta.preco_envelope * qtd + EnviaCarta.preco_selo * qtd
            self.saldo_selo += qtd
            self.saldo_envelope += qtd

        self.saldo -= preco_compra

    def diff_insumo_inicial(self):
        if self.saldo_selo > self.saldo_envelope:
            diff_qtd = self.saldo_selo - self.saldo_envelope
            self.compra_produto("envelope", diff_qtd)

        elif self.saldo_selo < self.saldo_envelope:
            diff_qtd = self.saldo_envelope - self.saldo_selo
            self.compra_produto("selo", diff_qtd)

    def compra_max_qtd_cartas(self):
        max_qtd_cartas = self.saldo // (EnviaCarta.preco_envelope + EnviaCarta.preco_selo)
        self.compra_produto("envelope e carta", max_qtd_cartas)

EnviaCarta.preco_envelope = PE
EnviaCarta.preco_selo = PS

envia_carta = EnviaCarta(RS, QS, QE)

envia_carta.diff_insumo_inicial()
envia_carta.compra_max_qtd_cartas()

cartas = envia_carta.saldo_envelope

print(int(cartas))
