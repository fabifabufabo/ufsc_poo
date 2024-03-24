

n_jogos = 1

resultados = str()

while n_jogos != 0:
    
    maria = 0

    joao = 0

    n_jogos = int(input())
    
    if n_jogos == 0:
    
        break
    
    resultados = input()

    resultados = resultados.split()

    for i in range(n_jogos):
        
        if int(resultados[i]) == 0:
            
            maria += 1
            
        else:
            
            joao += 1
            

    print(f"Mary won {maria} times and John won {joao} times")
