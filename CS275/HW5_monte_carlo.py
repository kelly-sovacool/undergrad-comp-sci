#!/usr/local/bin/python3
"""
Kelly Sovacool
CS275 HW5 bonus
15 July 2016
usage: ./monte_carlo.py <number_of_trials>
"""
from random import randrange
import time
from sys import argv


def main():
    start = time.time()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    trials = int(argv[1])
    successes = {'a':0, 'b':0, 'c':0}

    for i in range(trials):
        perm = random_perm(alphabet)
        successes['a'] += event_a(alphabet, perm)
        # Check whether a is the first letter of the permutation and z is the last letter.
        successes['b'] += 1 if perm[0] == 'a' and perm[25] == 'z' else 0
        # Check whether a and z are next to each other in the permutation.
        successes['c'] += 1 if perm.find('a') - perm.find('z') == (1 or -1) else 0

    for key, value in sorted(successes.items()):
        print("The probability of event", key, "occurring is", value, "/", trials)
        print("\t", str(100 * value / trials), "%")

    end = time.time()
    print(str(end - start), "secs")


def random_perm(alphabet):
    """
    Generate a random permutation of the alphabet
    """
    perm = ""
    while len(alphabet) > 0:
        letter = alphabet[randrange(len(alphabet))]
        perm += letter
        alphabet = alphabet.replace(letter, "")
    return perm


def event_a(alph, perm):
    """
    Check whether the first 13 letters of the permutation are in alphabetical order
    """
    prev = perm[0]
    isOrdered = 1
    i = 1
    while isOrdered and i < 13:
        curr = perm[i]
        if (alph.find(curr) - alph.find(prev)) != 1:
            isOrdered = 0
        prev = curr
        i += 1
    return isOrdered


main()
