

alfabeto_normal = input().lower()

alfabeto_cifrado = input().lower()

mensagem_cifrada = input().lower()

mensagem_decifrada = [alfabeto_normal[alfabeto_cifrado.index(x)] if x.isalpha() else x\
                      
                      for x in mensagem_cifrada]

print(''.join(mensagem_decifrada))