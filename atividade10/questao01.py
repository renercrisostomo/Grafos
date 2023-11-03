
"""
1ª QUESTÃO:
Implemente com a linguagem de sua preferência um programa em que dado dois grafos não dirigidos na forma de matriz de adjacência com vértices igual a 5 como entradas, o programa irá identificar se ambas são isomorfos ou não
"""

def ler_matriz_adjacencia(n):
    matrizAdjacencia = []
    for i in range(n):
        linha = input(f"Digite a linha {i+1} da matriz de adjacência ( ex: 1 0 1 0 1 ): ").strip().split()
        linha = [int(x) for x in linha]
        matrizAdjacencia.append(linha)
    return matrizAdjacencia

def is_isomorfo(matriz1, matriz2):
    if len(matriz1) != len(matriz2):
        return False
    
    graus1 = [sum(linha) for linha in matriz1]
    graus2 = [sum(linha) for linha in matriz2]
    graus1.sort()
    graus2.sort()
    if graus1 != graus2:
        return False
    
    arestas1 = sum([sum(linha) for linha in matriz1]) // 2
    arestas2 = sum([sum(linha) for linha in matriz2]) // 2
    if arestas1 != arestas2:
        return False
    
    return True

n = 5
print("Digite a matriz de adjacência do primeiro grafo:")
matriz1 = ler_matriz_adjacencia(n)
print("Digite a matriz de adjacência do segundo grafo:")
matriz2 = ler_matriz_adjacencia(n)

if is_isomorfo(matriz1, matriz2):
    print("Os grafos são isomorfos.")
else:
    print("Os grafos não são isomorfos.")
