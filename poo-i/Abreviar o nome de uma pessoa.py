

nome = input().split()

nome_abreviado = []

nome_abreviado.append(nome[0])

for i in nome[1:-1]:

    if len(i) > 3:
        
        nome_abreviado.append(i[0] + ".")
        
    else:
        
        nome_abreviado.append(i)

nome_abreviado.append(nome[-1])

print(*nome_abreviado)
        
        