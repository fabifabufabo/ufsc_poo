
entradas = []

entradas.append(input())
entradas.append(input())
entradas.append(input())
entradas.append(input())

valores_distintos = {}

for i in entradas:
    
    if i not in valores_distintos:
  
        valores_distintos[i] = 1
    
    else:
        
        valores_distintos[i] += 1
        
print(len(valores_distintos))


        

