M = int(input("Quantas linhas vai ter a primeira matriz? "))
N = int(input("Quantas colunas vai ter a primeira matriz? "))

# Garantir que a segunda matriz tenha as mesmas dimensões
print("A segunda matriz precisa ter as mesmas dimensões da primeira.")
B = M  # Número de linhas da segunda matriz
V = N  # Número de colunas da segunda matriz

# Inicialização das matrizes
mat1 = [[0 for x in range(N)] for x in range(M)]
mat2 = [[0 for x in range(N)] for x in range(M)]
mat_soma = [[0 for x in range(N)] for x in range(M)]  # Matriz para armazenar o resultado da soma

# Preenchendo a primeira matriz
print("Preenchendo a primeira matriz:")
for i in range(M):
    for j in range(N):
        mat1[i][j] = int(input(f"Elemento [{i},{j}] da primeira matriz: "))

# Preenchendo a segunda matriz
print("Preenchendo a segunda matriz:")
for i in range(M):
    for j in range(N):
        mat2[i][j] = int(input(f"Elemento [{i},{j}] da segunda matriz: "))

# Somando as duas matrizes
for i in range(M):
    for j in range(N):
        mat_soma[i][j] = mat1[i][j] + mat2[i][j]

# Exibindo o resultado
print("\nO RESULTADO DA SOMA DAS DUAS MATRIZES É:")
for i in range(M):
    for j in range(N):
        print(mat_soma[i][j], end="\t")
    print()  # Para pular para a próxima linha
