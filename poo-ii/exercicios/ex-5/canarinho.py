from ave import Ave

class Canarinho(Ave): 
    def __init__(self, tamanho_passo, altura_voo):
        super().__init__(tamanho_passo, altura_voo)
  

    def mover(self):
        return f"ANIMAL: DESLOCOU {self.tamanho_passo} VOANDO"
    
    def produzir_som(self):
        return "AVE: PRODUZ SOM: PIU"
        
    def cantar(self):
        return "AVE: PRODUZ SOM: PIU"
    