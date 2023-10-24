# qtd_idas = int(input())

qtd_produtos_disp = int(input())

produtos_disp = []
precos = []

for i in range(qtd_produtos_disp):
    produto_preco = input()

    produto_disp, preco = produto_preco.split()

    produtos_disp.append(produto_disp)
    precos.append(float(preco))

dic_produto_preco = {x: y for x, y in zip(produtos_disp, precos)}

qtd_produtos_dif = int(input())

preco_total = 0

for i in range(qtd_produtos_dif):
    produto_escolhido, quantidade = input().split()

    preco_total += dic_produto_preco[produto_escolhido] * quantidade
