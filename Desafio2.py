M: int
N: int
soma : float
numeros : float
M = int(input("Quantas linhas vai ter a matriz? "))
N = int(input("Quantas colunas vai ter a matriz? "))

numeros = 0
soma = 0
mat: [[int]] = [[0 for x in range(N)] for x in range(M)]
for i in range(0, M):
 for j in range(0, N):
    mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
    print()
print("O RESULTADO DA SOMA DESSA MATRIZ É:")
for i in range(0, M):
 for j in range(0, N):
    numeros = numeros + mat[i][j]



print(numeros)




