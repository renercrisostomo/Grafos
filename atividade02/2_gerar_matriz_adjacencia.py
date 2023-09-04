# Questão 2 - Desenvolva um programa em que gera uma matriz adjacência de um grafo completo dado como entrada (o usuário deve digitar) o valor de "m <= 9" que não pode ser negativo.
# OBS: "m" é valor do grafo completo.

def gerar_matriz_adjacencia(m):
  if m < 0 or m > 9:
    print("Valor inválido de m. Deve ser um inteiro entre 0 e 9.")
    return None
  matriz = []
  for i in range(m):
    matriz.append([0] * m)
  for i in range(m):
    for j in range(m):
      if i != j:
        matriz[i][j] = 1
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

m = int(input("Digite o valor de m: "))

matriz = gerar_matriz_adjacencia(m)

printar_matriz_adjacencia(matriz)
