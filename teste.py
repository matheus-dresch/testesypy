from math import ceil, floor
from random import random

print('Bem-vindo ao jogo!')
print('******************')

numero_secreto = round(random() * 100)
tentativas = 3

while (tentativas > 0):
    numero_usuario = int(input('-> Chute um número (entre 1 e 100): '))

    if (numero_usuario < 1 or numero_usuario > 100):
        print('--> Digite um número entre 1 e 100!')
        print('')
        continue

    if (numero_usuario == numero_secreto):
        print('--> ★ Boa! Você acertou.')
        break
    else:
        if (numero_usuario > numero_secreto):
            print('--> 🗙 Errou! O número é menor.')
        else:
            print('--> 🗙 Errou! O número é maior.')
        tentativas -= 1
        print('---> {:02d} tentativas restantes'.format(tentativas))
    print(' ')
print('---> ✓ Jogo finalizado com {:02d} tentativas(s) restantes, o número era: {}'.format(tentativas, numero_secreto))



