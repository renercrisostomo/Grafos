"""
2ª QUESTÃO:
Implemente um programa em que dado a matriz de adjacência de um grafo não dirigido como entrada,
o programa irá identificar se o grafo é regular ou não
"""

def ler_matriz_adjacencia(n):
    matrizAdjacencia = []
    for i in range(n):
        linha = input(f"Digite a linha {i+1} da matriz de adjacência ( ex: 1 0 1 1 ): ").strip().split()
        linha = [int(x) for x in linha]
        matrizAdjacencia.append(linha)
    return matrizAdjacencia

def verificar_grau_regular(matrizAdjacencia):
    n = len(matrizAdjacencia)
    grau = sum(matrizAdjacencia[0])
    for i in range(1, n):
        if sum(matrizAdjacencia[i]) != grau:
            return False
    return True

# n = int(input("Digite o número de nós do grafo: "))
# matrizAdjacencia = ler_matriz_adjacencia(n)
matrizAdjacencia = [[0, 1, 1, 1, 0, 0],
                    [1, 0, 1, 0, 1, 0],
                    [1, 1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1, 0],
                    [0, 1, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0]]

print("O grafo é representado pela matriz de adjacência:")
for linha in matrizAdjacencia:
    print(linha)
if verificar_grau_regular(matrizAdjacencia):
    print("O grafo é regular.")
else:
    print("O grafo não é regular.")
