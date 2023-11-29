"""
3ª QUESTÃO:
Implemente um programa em que dado a matriz de incidência de um grafo não dirigido como entrada, o programa irá identificar quantos nós dará para fazer uma redução em série?
"""

import numpy as np

def serie_reducao(matriz):
    n_linhas, n_colunas = matriz.shape
    
    n_reduziveis = 0
    
    for i in range(n_linhas):
        if np.sum(matriz[i, :]) == 2:
            n_reduziveis += 1
    
    return n_reduziveis

matriz = np.array([[1, 1, 1, 0, 0, 0, 0],
                   [1, 0, 0, 1, 1, 0, 0],
                   [0, 1, 0, 1, 0, 0, 1],
                   [0, 0, 1, 0, 1, 1, 1],
                   [0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 1]])

print("O número de nós que podem ser reduzidos em série é:", serie_reducao(matriz))
