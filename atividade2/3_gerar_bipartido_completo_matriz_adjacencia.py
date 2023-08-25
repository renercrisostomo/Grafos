# Questão 3 - Desenvolva uma matriz de adjacência do grafo bipartido completo

def gerar_matriz_adjacencia_bipartido(m, n):
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

def printar_matriz_adjacencia(matriz):
  for i in range(len(matriz)):
      for j in range(len(matriz)):
          if matriz[i][j] > 0:
              print(f"{i}{j} = 1\t", end="")
          else:
              print(f"{i}{j} = 0\t", end="")
      print("\n")
  print("\n")

m = int(input("Digite o número de vértices da primeira partição: "))
n = int(input("Digite o número de vértices da segunda partição: "))

matriz = gerar_matriz_adjacencia_bipartido(m, n)

printar_matriz_adjacencia(matriz)
