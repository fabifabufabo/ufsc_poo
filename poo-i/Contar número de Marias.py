

n_entradas = int(input())

nome = ""

contagem = 0 

for i in range(n_entradas):
    
    nome = input()
    
    nome_partes = nome.split()
    
    if "Maria" in nome_partes:
        
        contagem += 1
        
        
print(contagem)       