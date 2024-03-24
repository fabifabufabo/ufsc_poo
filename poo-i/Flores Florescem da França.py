

entrada = input().lower().split()

primeira_palavra = entrada[0]

primeira_letra = primeira_palavra[0]

n_eh_tautograma = 0

for palavra in entrada:
        
    if palavra[0] != primeira_letra:
            
         n_eh_tautograma += 1
         
if n_eh_tautograma > 0:
    
    print("N")
    
else:
    
    print("Y")
            
        
