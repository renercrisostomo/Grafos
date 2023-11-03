"""
1ª QUESTÃO:
Faça uma implementação na linguagem de sua preferencia em que o usuário irá digitar uma matriz de adjacência de tamanho 6x6 como entrada (input) representada por um "grafo dirigido de 6 nós", após isso o programa deverá imprimir a quantidade de graus de entradas e saídas de cada nó
"""

def ler_matriz(n):
    matriz = []
    for i in range(n):
        linha = input(f"Digite a {i+1}ª linha da matriz 1,-1,0,1...: ").split()
        linha = [int(x) for x in linha]
        matriz.append(linha)
    return matriz

def calcular_graus(matriz):
    n = len(matriz)
    graus_entrada = [0] * n
    graus_saida = [0] * n
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == -1:
                graus_saida[i] += 1
            elif matriz[i][j] == 1:
                graus_entrada[i] += 1
    return graus_entrada, graus_saida

n = 6
matriz = ler_matriz(n)
graus_entrada, graus_saida = calcular_graus(matriz)
print("Os graus de entrada de cada nó são:")
for i in range(n):
    print(f"Nó {i+1}: {graus_entrada[i]}")
print("Os graus de saída de cada nó são:")
for i in range(n):
    print(f"Nó {i+1}: {graus_saida[i]}")
