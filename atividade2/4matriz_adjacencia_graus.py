def matriz_adjacencia_graus(arestas):
  if not arestas or not isinstance(arestas, list):
    print("Lista de arestas inválida. Deve ser uma lista não vazia de tuplas.")
    return None, None
  max_vertice = max(max(a, b) for a, b in arestas)
  matriz = []
  for i in range(max_vertice + 1):
    matriz.append([0] * (max_vertice + 1))
  graus = [0] * (max_vertice + 1)
  for a, b in arestas:
    matriz[a][b] = 1
    matriz[b][a] = 1
    graus[a] += 1
    graus[b] += 1
  return matriz, graus

arestas = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 5), (3, 5), (4, 5)]

matriz, graus = matriz_adjacencia_graus(arestas)
if matriz is not None and graus is not None:
  print("A matriz de adjacência do grafo é:")
  for linha in matriz:
    print(linha)
  print("A lista de graus dos vértices é:")
  print(graus)
