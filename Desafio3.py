numeros = [32, 10, 58, 30, 55, 12, 28, 51]

escolha = int(input("Escolha:\n 1 - pares primeiro seguidos pelos ímpares\n 2 - ordem crescente\n"))

if escolha == 1:
    numeros.sort()
    print(f"Os numeros em ordem crescente da lista é:", numeros)
else:
    for i in numeros:
        resultado = i % 2
        if resultado == 0:
            print(f"{i} ")

for i in numeros:
    resultado = i % 2
    if resultado != 0:
        print(f'{i}')