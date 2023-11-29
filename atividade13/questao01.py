"""
1ª QUESTÃO:
Implemente com a linguagem de sua preferência um programa em que dado um grafos não dirigidos na forma de matriz de adjacência com vértices igual a 5 como entradas, verificar se o grafo é regular, após a validação do grafo regular o programa irá mostrar se o mesmo é planar?
"""

def ler_matriz_adjacencia(n):
    matrizAdjacencia = []
    for i in range(n):
        linha = input(f"Digite a linha {i+1} da matriz de adjacência ( ex: 1 0 1 0 1 ): ").strip().split()
        linha = [int(x) for x in linha]
        matrizAdjacencia.append(linha)
    return matrizAdjacencia

def is_regular(matriz):
    graus = [sum(linha) for linha in matriz]
    return all(grau == graus[0] for grau in graus)

def is_planar(matriz):
    graus = [sum(linha) for linha in matriz]
    return all(grau <= 2 for grau in graus)


# n = int(input("Digite o número de nós do grafo: "))
# matrizAdjacencia = ler_matriz_adjacencia(n)
matrizAdjacencia = [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]]

if is_regular(matrizAdjacencia):
    print("O grafo é regular.")
    if is_planar(matrizAdjacencia):
        print("O grafo é planar.")
    else:
        print("O grafo não é planar.")
else:
    print("O grafo não é regular.")
