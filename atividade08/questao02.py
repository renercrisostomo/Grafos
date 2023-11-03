"""
2ª QUESTÃO:
Faça um algoritmo para o grafo da questão 1, em que conta quantos componentes conexos existem
PS: Pode usar qualquer estrutura de grafos.

1 - 2, 4, 5
2 - 1, 3, 5
3 - 2, 9
4 - 1, 5
5 - 1, 2, 4
6 - 7, 8
7 - 6, 8
8 - 6, 7
9 - 3
"""

def ler_lista_adjacencia(n):
    listaAdjacencia = []
    for i in range(n):
        linha = input(f"Digite os nós adjacentes ao nó {i+1} ( ex: 1,-1,0,1 ): ").strip().split(',')
        linha = [int(x) for x in linha]
        listaAdjacencia.append(linha)
    return listaAdjacencia

def encontrar_componentes_conexos(listaAdjacencia):
    n = len(listaAdjacencia)
    visitados = [False] * n
    componentesConexos = []
    for i in range(n):
        if not visitados[i]:
            componente = []
            visitados[i] = True
            fila = [i]
            while len(fila) > 0:
                no = fila.pop(0)
                componente.append(no+1)
                for vizinho in listaAdjacencia[no]:
                    if vizinho > 0 and not visitados[vizinho-1]:
                        visitados[vizinho-1] = True
                        fila.append(vizinho-1)
            componentesConexos.append(componente)
    return componentesConexos

# n = int(input("Digite o número de nós do grafo: "))
# listaAdjacencia = ler_lista_adjacencia(n)
listaAdjacencia = [[2, 4, 5],
                   [1, 3, 5],
                   [2, 9],
                   [1, 5],
                   [1, 2, 4],
                   [7, 8],
                   [6, 8],
                   [6, 7],
                   [3]]

print("O grafo é representado pela listaAdjacencia:")
for linha in listaAdjacencia:
    print(linha)
componentesConexos = encontrar_componentes_conexos(listaAdjacencia)
print(f"O grafo possui {len(componentesConexos)} componentes conexos.")
print("Os componentes conexos são:")
for componente in componentesConexos:
    print(componente)

