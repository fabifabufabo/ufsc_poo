def eh_anagrama(palavra1, palavra2):
    
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    return sorted(palavra1) == sorted(palavra2)

palavra1 = input()
palavra2 = input()

resultado = eh_anagrama(palavra1, palavra2) and palavra1 != palavra2

print(resultado)