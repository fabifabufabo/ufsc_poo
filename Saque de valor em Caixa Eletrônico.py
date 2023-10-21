

n_entradas = int(input())

valor_qtd_cedulas = {}

for i in range(n_entradas):
    
    chave = float(input())
    valor_qtd_cedulas[chave] = None
    
    valor = int(input())
    valor_qtd_cedulas[chave] = valor

valor_saque = float(input())

qtd_cedulas = 0

saida = []

for i in sorted(valor_qtd_cedulas.keys(), reverse=True):
    
    qtd_cedulas = valor_saque // i
    
    if qtd_cedulas <= valor_qtd_cedulas[i]:
        
        valor_saque -= qtd_cedulas * i 
    
        saida.append(int(qtd_cedulas))
        
    else:
        
        saida.append(int(0))
    
saida.reverse()
    
print(*saida, sep=' ')
