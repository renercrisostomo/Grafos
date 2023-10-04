"""
3ª QUESTÃO:
Implemente uma lista de adjacência do grafo direcionado abaixo, ainda conte quantos graus tem em
cada nó(saída e entrada)?

A -> V e C
V -> D e W
C -> W
D -> F
W -> F

lista de adjacência do grafo

0 -> 1 e 2
1 -> 3 e 4
2 -> 4
3 -> 5
4 -> 5
5 ->
"""

def ler_lista_adjacencia(n):
    listaAdjacencia = []
    for i in range(n):
        linha = input(f"Digite os nós adjacentes ao nó {i+1} ( ex: 1,-1,0,1 ): ").strip().split(',')
        linha = [int(x) for x in linha]
        listaAdjacencia.append(linha)
    return listaAdjacencia

def graus(lista_adjacencia):
    graus = [0] * len(lista_adjacencia)
    for i in range(len(lista_adjacencia)):
        for j in range(len(lista_adjacencia[i])):
            graus[lista_adjacencia[i][j]] += 1
    return graus

# n = int(input("Digite o número de nós do grafo: "))
# listaAdjacencia = ler_lista_adjacencia(n)
lista_adjacencia = [
    [1, 2],
    [3, 4],
    [4],
    [5],
    [5],
    []
]

print(graus(lista_adjacencia))
