
teste = 1

while True:
    
    total_aero, total_voo = map(int, input().split())
    if total_aero == total_voo == 0:
        break
    
    lista_aero = {x: 0 for x in range(1, total_aero + 1)}
    
    origem = 0
    
    destino = 0

    for i in range(total_voo):

        origem, destino = map(int, input().split())
        lista_aero[origem] += 1
        lista_aero[destino] += 1
    
    maior_movimento = max(lista_aero, key=lista_aero.get)
    
    aero_mais_movimentado = [x for x in range(1, total_aero + 1) \
                            if lista_aero.get(x) == lista_aero.get(maior_movimento)]
    
    lista_aero.get(2) 
    
    print(f"Teste {teste}")
    print(*aero_mais_movimentado)
    print()
    
    teste += 1
