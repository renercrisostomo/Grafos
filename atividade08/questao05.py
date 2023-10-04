"""
5ª QUESTÃO:
Implemente com a linguagem de sua preferência 2 ordenações topológica do “grafo e a estrutura(lista
de adjacência da questão 3”

A -> V e C
V -> D e W
C -> W
D -> F
W -> F
F ->

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

def contar_graus(lista_adjacencia):
    graus = [0] * len(lista_adjacencia)
    for i in range(len(lista_adjacencia)):
        for j in range(len(lista_adjacencia[i])):
            graus[lista_adjacencia[i][j]] += 1
    return graus

def ordenacao_topologica(lista_adjacencia):
    graus = contar_graus(lista_adjacencia)

    fila = []
    for i in range(len(graus)):
        if graus[i] == 0:
            fila.append(i)

    ordenacao = []
    while len(fila) > 0:
        vertice = fila.pop(0)
        ordenacao.append(vertice)
        for i in range(len(lista_adjacencia[vertice])):
            graus[lista_adjacencia[vertice][i]] -= 1
            if graus[lista_adjacencia[vertice][i]] == 0:
                fila.append(lista_adjacencia[vertice][i])

    return ordenacao

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

print(ordenacao_topologica(lista_adjacencia))
