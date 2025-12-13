import random

NUM_DIGITS =3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic Game
            By Al Sweigart
            I am thinking of a {}-digit number with no repeated digits.
          Try tp guess what it is. Here are some clues:
          When I say:    That means:
          Pico         One digit is correct but in the wrong position.
            Fermi        One digit is correct and in the right position.
            Bagels       No digit is correct.
            For example, if the secret number was 248 and your guess was 843, the
            clues would be Fermi Pico.'''.format(NUM_DIGITS))
    
    