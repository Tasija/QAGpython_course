from random import randint
from math import log2


def start_game():
    print('Do you want to play a game?')
    while True:
        try:
            max_num = int(
                input("Please choose the game range from 1 till ...: "))
            break
        except ValueError:
            continue

    secret_number = randint(0, max_num)
    tries = int(log2(max_num + 1)) + 1
    print('You have {} tries'.format(tries))
    return guessingGame(secret_number, tries)


def guessingGame(secret_number, tries):

    if tries == 0:
        return print('No more tries left. My number was {}'.format(secret_number))

    user_input = input("Try to guess: ")

    if int(user_input) == secret_number:
        return print('You guess my number!')
    elif secret_number > int(user_input):
        print ("My number is higher.")
        print ('You have {} tries'.format(tries - 1))
    else:
        print ("My number is lower.")
        print ('You have {} tries'.format(tries - 1))
    guessingGame(secret_number, tries - 1)


start_game()
