
qtd_testes = int(input())

def operacao(a, operador, b):

    a = int(a)
    b = int(b)

    if operador == "+":
        return a + b

    elif operador == "-":
        return a - b

    else:
        return a * b



for i in range(qtd_testes):

    conta, resultado = input().split(sep = "=")

    a, operador, b = conta.split()

    resposta_correta = operacao(a, operador, b)

    if int(resultado) != resposta_correta:

        diferenca = abs(int(resultado) - resposta_correta)

        print("E" + "r" * diferenca + "ou!")



