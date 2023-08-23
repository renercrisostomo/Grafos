def matriz_adjacencia_bipartido(m, n):
  if m < 0 or n < 0:
    print("Números inválidos de vértices. Devem ser inteiros não negativos.")
    return None
  matriz = []
  for i in range(m + n):
    matriz.append([0] * (m + n))
  for i in range(m):
    for j in range(m, m + n):
      matriz[i][j] = 1
      matriz[j][i] = 1
  return matriz

m = int(input("Digite o número de vértices da primeira partição: "))
n = int(input("Digite o número de vértices da segunda partição: "))

matriz = matriz_adjacencia_bipartido(m, n)
if matriz is not None:
  print("A matriz de adjacência do grafo bipartido completo é:")
  for linha in matriz:
    print(linha)
