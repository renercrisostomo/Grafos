# Questão 4 - Implemente uma matriz de adjacência do grafo abaixo e aplique a contagem dos graus de cada nó.
# N = {0, 1, 2, 3, 4, 5}
# A = {a1, a2, a3, a4, a5, a6, a7}
# g(a1) = {0, 1},
# g(a2) = {0, 2},
# g(a3) = {0, 3},
# g(a4) = {1, 2},
# g(a5) = {1, 4},
# g(a6) = {3, 4},
# g(a7) = {3, 5}

def listar_arestas(matriz):
  """
  [[0, 1, 1, 1, 0, 0],
   [1, 0, 1, 0, 1, 0],
   [1, 1, 0, 0, 0, 0],
   [1, 0, 0, 0, 1, 1],
   [0, 1, 0, 1, 0, 0],
   [0, 0, 0, 1, 0, 0]] -> [(0,1), (0,2), (0,3), (1,2), (1,4), (3,4), (3,5)]
  """
  arestas = []
  for i in range(len(matriz)):
    for j in range(i+1, len(matriz)):
      if matriz[i][j] > 0:
        arestas.append((i, j))
  arestas_sem_repeticao = list(set([tuple(sorted(aresta)) for aresta in arestas]))
  print(arestas_sem_repeticao)
  return arestas_sem_repeticao

def listar_graus(arestas):
  """
  [(0,1), (0,2), (0,3), (1,2), (1,4), (3,4), (3,5)] -> [3, 3, 2, 3, 2, 1]
  """
  lista_graus = []
  for aresta in arestas:
    for vertice in aresta:
      if vertice > len(lista_graus) - 1:
        lista_graus.append(1)
      else:
        lista_graus[vertice] += 1
  print(lista_graus)

  return lista_graus

def printar_matriz_adjacencia(matriz):
  for i in range(len(matriz)):
      for j in range(len(matriz)):
          if matriz[i][j] > 0:
              print(f"{i}{j} = 1\t", end="")
          else:
              print(f"{i}{j} = 0\t", end="")
      print("\n")
  print("\n")

matriz = [
  [0, 1, 1, 1, 0, 0],
  [1, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1],
  [0, 1, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0]
]

printar_matriz_adjacencia(matriz)
arestas = listar_arestas(matriz)
graus_por_vertice = listar_graus(arestas)

print(graus_por_vertice)
