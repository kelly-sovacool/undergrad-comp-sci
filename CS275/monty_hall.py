#!/usr/local/bin/python3
"""
Kelly Sovacool
12 July 2016
usage: ./monty_hall.py <number_of_iterations>
"""
from random import randrange
from sys import argv
import time


def play(player):
    doors = [x for x in range(3)]
    car = randrange(3)  # place car behind a pseudo-random door
    goats = list(doors)
    goats.remove(car)  # goats = doors - car
    guess1 = randrange(3)  # 1st guess is pseudo-random

    # pick a goat to reveal
    revealed_goat = list(goats)
    if guess1 in goats:
        revealed_goat.remove(guess1)
        revealed_goat = revealed_goat[0]
    else:
        revealed_goat = goats[randrange(2)]
    doors.remove(revealed_goat)

    # 2nd guess
    if player == 'swap':
        # swap doors
        doors.remove(guess1)
        guess2 = doors[0]
    else:
        # stay
        guess2 = guess1

    # end game
    if guess2 == car:
        player_wins = 1
    else:
        player_wins = 0

    return player_wins


def main():

    start = time.time()
    iterations = int(argv[1])
    swap_wins = 0
    stay_wins = 0
    for i in range(iterations):
        swap_wins += play('swap')
        stay_wins += play('')
    swap_percent = 100 * swap_wins / iterations
    stay_percent = 100 * stay_wins / iterations
    stop = time.time()

    print('Monty Hall Probability')
    print('Player that swapped on 2nd guess won', str(swap_wins), '/', str(iterations), 'games:', swap_percent, '%')
    print('Player that kept their 1st guess won', str(stay_wins), '/', str(iterations), 'games:', stay_percent, '%')
    print('runtime:', round(stop - start, 2), 'secs')


main()
