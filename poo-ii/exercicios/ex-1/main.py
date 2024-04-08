

class Ordenacao:

    # Recebe o array com o conteudo a ser ordenado
    def __init__(self, array_para_ordenar):
        self.array = array_para_ordenar

    # Realiza a ordenacao do conteudo do array recebido no construtor
    def ordena(self):
        
        array = self.array

        n = len(array)

        for i in range(n):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

        return array

    # Converte o conteudo do array em String formatado
    def toString(self):

        array_sorteado = self.ordena()        
        return ','.join(map(str, array_sorteado))
    
array_para_ordenar = [4, 0, 0, 2, 8, 9, 2, 2]
ordenador = Ordenacao(array_para_ordenar)
print(ordenador.toString())
