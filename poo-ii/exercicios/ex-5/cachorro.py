from mamifero import Mamifero

class Cachorro(Mamifero): 
    def __init__(self, tamanho_passo=3, volume_som=3):
        super().__init__(tamanho_passo, volume_som)


    def mover(self):
        return f"ANIMAL: DESLOCOU {self.tamanho_passo}"

    def produzir_som(self):
        return "MAMIFERO: PRODUZ SOM: "
		
    def latir(self):
        return f"MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: AU"