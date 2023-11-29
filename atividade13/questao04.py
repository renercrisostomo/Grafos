"""
4ª QUESTÃO:
Implemente um programa em que dado a matriz de adjacência de um grafo não dirigido como entrada, o programa irá mostrar quantas bordas existem no grafo?
"""

import numpy as np

def numero_bordas(matriz):
    n_linhas = matriz.shape[0]
    
    n_arestas = 0
    
    for i in range(n_linhas):
        n_arestas += np.sum(matriz[i, :])
    
    n_arestas //= 2
    
    return n_arestas

matriz = np.array([[0, 1, 0, 1, 1, 0, 0],
                   [1, 0, 1, 1, 0, 0, 0],
                   [0, 1, 0, 1, 0, 0, 1],
                   [1, 1, 1, 0, 1, 1, 1],
                   [1, 0, 0, 1, 0, 1, 0],
                   [0, 0, 0, 1, 1, 0, 0],
                   [0, 0, 1, 1, 0, 1, 0]])

print("O número de bordas do grafo é:", numero_bordas(matriz))

