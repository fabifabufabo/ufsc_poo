
acertos = 0

resposta = input()

gabarito = input()
        
for n in range(len(resposta)):
    
    if resposta[n] == gabarito[n]:
        
        acertos += 1
        
print(acertos)
    
    
    
    
    