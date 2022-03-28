from random import randrange


print('--> FORCAPY <--')
print('---------------')

words_doc = open('palavras.txt', 'r')
words_array = []

for linha in words_doc:
    words_array.append(linha)

rand_index = randrange(0, len(words_array))
secret_word = words_array[rand_index].strip()

correct_letters = ["_" for letra in secret_word]

print('Palavra a ser acertada:')
print('->', " ".join(correct_letters))

tentativas_totais = 6
tentativas = tentativas_totais

while (True):
    letra = input('Chute uma letra: \n').strip().lower()

    if (not letra) or (len(letra) > 1):
        print('Letra inválida \n')
        continue

    if (letra not in secret_word): 
        print('Letra não está na palavra.')
        tentativas -= 1

        if (tentativas == 0):
            print('Enforcou! O jogo acabou. A palavra era: {}'.format(secret_word))
            break

        print('{} tentativas restantes. \n'.format(tentativas))
        continue

    for i in range(len(secret_word)):
        if(secret_word[i-1] == letra):
            correct_letters[i-1] = letra.upper()
    
    print(" ".join(correct_letters), '\n')

    if ("".join(correct_letters).lower() == secret_word):
        print('Parabéns! Você acertou a palavra.')
        break