"""
1ª QUESTÃO:
Implemente o algoritmo usando lista de adjacência para modelar o grafo abaixo ?


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

n = int(input("Digite o número de nós do grafo: "))
listaAdjacencia = ler_lista_adjacencia(n)
print("O grafo é representado pela listaAdjacencia:")
for linha in listaAdjacencia:
    print(linha)
