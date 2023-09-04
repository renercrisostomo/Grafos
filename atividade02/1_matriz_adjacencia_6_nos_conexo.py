# Questão 1 - Implemente uma matriz de adjacência de um grafo não dirigido com 6 nós em que seja conexo

def printar_matriz_adjacencia(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] > 0:
                print(f"{i}{j} = 1\t", end="")
            else:
                print(f"{i}{j} = 0\t", end="")
        print("\n")
    print("\n")

matriz = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

printar_matriz_adjacencia(matriz)