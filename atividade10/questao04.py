"""
4ª QUESTÃO:
Implemente um programa em que dado dois índices "m" e "n" como entradas em que representam os conjuntos de nós de um grafo bipartido, o programa irá mostrar a matriz de incidência desse grafo bipartido
"""


def gerar_matriz_incidencia_bipartido(m, n):
    if m < 0 or n < 0:
        print("Números inválidos de vértices. Devem ser inteiros não negativos.")
        return None
    matriz = []
    for i in range(m):
        matriz.append([0] * (m + n))
    for i in range(m):
        for j in range(m, m + n):
            matriz[i][j] = 1
    return matriz


def printar_matriz_incidencia(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}\t", end="")
        print("\n")
    print("\n")


m = int(input("Digite o número de vértices da primeira partição: "))
n = int(input("Digite o número de vértices da segunda partição: "))

matriz = gerar_matriz_incidencia_bipartido(m, n)

printar_matriz_incidencia(matriz)
