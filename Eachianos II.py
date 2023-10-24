

qtd_textos = int(input())
palavra_buscada = str()
index_palavra = str()

for i in range(qtd_textos):

    texto = input()
    palavra_buscada = input() + ' '

    index_palavra = texto.index(palavra_buscada)
    print(index_palavra)