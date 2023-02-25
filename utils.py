import random


def get_secret_num(max_digits):
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_number = ''

    for i in range(max_digits):
        secret_number += str(numbers[i])

    return secret_number


def get_clues(guess, secret_number):
    if guess == secret_number:
        return 'You got it'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Pico')
        elif guess[i] in secret_number:
            clues.append('Fermi')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)







