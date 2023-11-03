"""
3ª QUESTÃO:
Implemente um programa em que dado a matriz de incidência de um grafo não dirigido como entrada, o programa irá identificar se o grafo é roda ou não
"""

def ler_matriz_incidencia(n, m):
    matrizIncidencia = []
    for i in range(n):
        linha = input(f"Digite a linha {i+1} da matriz de incidência ( ex: 1,-1,0,1 ): ").strip().split(',')
        linha = [int(x) for x in linha]
        matrizIncidencia.append(linha)
    return matrizIncidencia

def graus(matriz_incidencia):
    graus_vertices = [0] * len(matriz_incidencia)
    for j in range(len(matriz_incidencia[0])):
        count = 0
        for i in range(len(matriz_incidencia)):
            if matriz_incidencia[i][j] == 1:
                count += 1
        if count == 2:
            for i in range(len(matriz_incidencia)):
                if matriz_incidencia[i][j] == 1:
                    graus_vertices[i] += 1
    return graus_vertices

def is_conexo(matriz_incidencia):
    n = len(matriz_incidencia)
    m = len(matriz_incidencia[0])
    arestas = []
    for i in range(n):
        for j in range(m):
            if matriz_incidencia[i][j] == 1:
                arestas.append((i,j))
    visitados = [False] * n
    fila = [0]
    visitados[0] = True
    while fila:
        u = fila.pop(0)
        for aresta in arestas:
            if aresta[0] == u and not visitados[aresta[1]]:
                visitados[aresta[1]] = True
                fila.append(aresta[1])
    return all(visitados)

def is_roda(matriz_incidencia):
    n = len(matriz_incidencia)
    m = len(matriz_incidencia[0])
    if not is_conexo(matriz_incidencia):
        return False
    graus_vertices = graus(matriz_incidencia)
    central = None
    for i in range(n):
        if graus_vertices[i] == n-2:
            if central is None:
                central = i
            else:
                return False
        elif graus_vertices[i] != n-1:
            return False
    return central is not None

# n = int(input("Digite o número de nós do grafo: "))
# m = int(input("Digite o número de arestas do grafo: "))
# matrizIncidencia = ler_matriz_incidencia(n, m)
matriz_incidencia = [
    [1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1]
]

if is_roda(matriz_incidencia):
    print("O grafo é uma roda")
else:
    print("O grafo não é uma roda")
