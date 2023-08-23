def gera_matriz_adjacencia(m):
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

m = int(input("Digite o valor de m: "))

matriz = gera_matriz_adjacencia(m)
if matriz is not None:
  print("A matriz adjacência do grafo completo é:")
  for linha in matriz:
    print(linha)
