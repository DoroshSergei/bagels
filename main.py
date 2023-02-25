from utils import get_secret_num, get_clues


NUM_DIGITS = 3
MAX_GUESS = 10


def main():
    print(f'''Bagels, a deductive logic game.
    By Sergei Dorash serega7031435@gmail.com
    I am thinking of a {NUM_DIGITS} digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That mens:
    Pico        One digit is correct but in the wrong position
    Fermi       One digit is correct and in right position
    Bagels      No digit is correct

    For example, if the secret number was 248 and you guess was 843, the
    clues would be Fermi Pico''')

    while True:
        secret_number = get_secret_num(NUM_DIGITS)
        print('I have thought up a number.')
        print(f'You have {MAX_GUESS} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESS:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input('< ')

            clues = get_clues(guess, secret_number)
            print(clues)
            num_guesses += 1

            if guess == secret_number:
                break

            if num_guesses > MAX_GUESS:
                print('You ran out of guesses')
                print(f'The answer was {secret_number}')

        print('Do you want to play again& (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

    print('Thank you for playing!')


if __name__ == '__main__':
    main()


