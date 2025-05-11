#JogoDeAdivinhacao

import random

numeroIn : float
numeroSorteado = random.randint(1, 100)

vidas = 10

numeroIn = int(input('Digite um numero:'))

while numeroIn != numeroSorteado:
    if vidas <=1:
        print("Suas vidas acabaram, voce perdeu o jogo!")
        exit()
    else:
        if numeroIn > numeroSorteado:
            print("numero errado, o numero é menor")
            vidas = vidas - 1
        elif numeroIn < numeroSorteado:
            print("numero errado, o numero é maior")
            vidas = vidas-1

        numeroIn = int(input('Digite outro numero:'))

print("numero correto, parabens!")

