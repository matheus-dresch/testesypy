import random 
import pyperclip3 as pc

def generateRand():
    return random.randrange(1,101)

def levelChoose():
    while True:
        print('1 - Fácil | 2 - Médio | 3 - Difícil')
        level = int(input('-> Selecione o nível: '))

        if not (level >= 1 and level <= 3):
            print('⚠ Escolha inválida.')
            print('')
        else:
            break
    
    if (level == 1):
        return 12
    elif (level == 2):
        return 9
    elif (level == 3):
        return 6

print('-      NUMLE      -')
print('-------------------')
print('-> Nº entre 1 e 100')
print('-------------------')
print('')

total_tries = levelChoose()
tries = total_tries
tries_array = []
rand_num = generateRand()

while (tries >= 0):
    user_input = input('Digite um número: ')

    if (not user_input.isnumeric()):
        print('Digite um número válido.')
        print('')
        continue
    
    user_number = int(user_input)

    if (user_number == rand_num):
        print('🟩 Parabéns! Você acertou o número. 🟩')
        break
    
    higher = user_number > rand_num
    if (higher):
        num_is_str = 'menor'
    else:
        num_is_str = 'maior'
    
    num_diff = abs(user_number - rand_num) 
    
    if (num_diff > 0 and num_diff <= 15):
        print('Errou! O número é {}. 🟩'.format(num_is_str))
        tries_array.append('🟩')
    elif (num_diff > 15 and num_diff <= 30):
        print('Errou! O número é {}. 🟨'.format(num_is_str))
        tries_array.append('🟨')
    else:
        print('Errou! O número é {}. 🟥'.format(num_is_str))
        tries_array.append('🟥')

    tries -= 1

    print('')
    print('⚠ Você ainda tem {} de {} tentativas.'.format(tries, total_tries))
    print('-----------------------------------')

    if (tries == 0):
        print('🟥 Suas tentativas acabaram, o número era: {} :( 🟥'.format(rand_num))
        print('')
        play_again = input('Jogar novamente? s/n')
        if (play_again == 's'):
            total_tries = levelChoose()
            tries = total_tries
            tries_array = []
            rand_num = generateRand()
        else:
            break

pc.copy('numle.py #{}/{}.\n{}'.format(tries, total_tries, '\n'.join(tries_array)))