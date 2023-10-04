"""
4ª QUESTÃO:
Implemente o algoritmo, em que a entrada é uma matriz de incidência com 4 nós 6 arestas de um
grafo não dirigido, o programa vai mostrar a quantidade componentes conexos do grafo?
"""

def printar_matriz_incidencia(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 0:
                print(f"{i}{j} = 1\t", end="")
            else:
                print(f"{i}{j} = 0\t", end="")
        print("\n")
    print("\n")

def encontrar_componentes_conexos(matriz):
    numNos = len(matriz)
    numArestas = len(matriz[0])
    componentes = []
    for i in range(numNos):
        for j in range(numArestas):
            if matriz[i][j] == 1:
                if i not in componentes:
                    componentes.append(i)
                if j not in componentes:
                    componentes.append(j)
    return componentes

numNos = 4
numArestas = 6
matriz = [[1, 1, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 0, 0, 1, 1, 1],
          [1, 0, 1, 0, 1, 0]]

printar_matriz_incidencia(matriz)

componentes = encontrar_componentes_conexos(matriz)
print(f"O grafo possui {len(componentes)} componentes conexos.")
print(f"Os componentes conexos são:")
for componente in componentes:
    print(componente)
