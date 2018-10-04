'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Section: 006
Purpose:
Preconditions:
Postconditions:
Date:
'''
# Import randrange function to generate slot spins
from random import randrange
# Import graphics library to construct the user interface

def get_name():
    # 1. Input the player's name
    name = input("What's your name? ")
    # 2. return the player's name
    return name

def play_again():
    # 1. Initialize flag for valid input as False
    isInputValid = False
    # 2. while flag for valid input is False:
    while isInputValid == False:
        # 2.1 Input y, Y, n, or N
        answer = input('Do you want to play again? ')
        # 2.2 if input is 'y' or 'Y':
        if answer == 'y' or answer == 'Y':
            # 2.2.1 assign True to play again variable
            wantsToPlayAgain = True
            # 2.2.2 assign True to valid input flag to end the while loop
            isInputValid = True          
        # 2.3 else if input is 'n' or 'N':
        elif answer == 'n' or answer == 'N':
            # 2.3.2 assign False to play again variable
            wantsToPlayAgain = False
            # 2.3.1 assign True to valid input flag to end the while loop
            isInputValid = True           
        # 2.4 else:
        else:
            # 2.4.1 output 'Please enter N or n or Y or y'
            print('Please enter N or n or Y or y')
    # 3. return play again variable
    return wantsToPlayAgain

def get_bet(pot):
    # 1. Initialize flag for valid bet to False
    isBetValid = False
    # 2. while valid bet flag is False:
    while isBetValid == False:
        # 2.1 input the amount of the user's bet
        bet = int(input('How much do you want to bet (up to ' + str(pot) + ')? '))
        # 2.2 display 'Pull the lever! (press Enter)'
        input('Pull the lever! (press Enter)')   
        # 2.3 If bet is greater than pot:
        if bet > pot:
            # 2.3.1 Output "That's too much"
            print("That's too much")
        # 2.4 Else if bet is less than or equal to zero:
        elif bet <= 0:
            # 2.4.1 Output "That's too small"
            print("That's too small")
        # 2.5 Else:
        else:
            # 2.5.1 assign True to valid bet flag to end the while loop
            isBetValid = True
    # 3. return bet amount
    return bet

def translate(randNum):
    # 1. If random number is 0:
    if randNum == 0:
        # 1.1 assign 'apple' to symbol
        symbol = 'apple'
    # 2. Else if random number is 1:
    elif randNum == 1:
        # 2.1 assign 'banana' to symbol
        symbol = 'banana'
    # 3. Else if random number is 2:
    elif randNum == 2:
        # 3.1 assign 'cherry' to symbol
        symbol = 'cherry'
    # 4. Else if random number is 3:
    elif randNum == 3:
        # 4.1 assign 'grapes' to symbol
        symbol = 'grapes'
    # 5. Else if random number is 4:
    elif randNum == 4:
        # 5.1 assign 'lemon' to symbol
        symbol = 'lemon'
    # 6. Else if random number is 5:
    elif randNum == 5:
        # 6.1 assign 'melon' to symbol
        symbol = 'melon'
    # 7. Else if random number is 6:
    elif randNum == 6:
        # 7.1 assign 'orange' to symbol
        symbol = 'orange'
    # 8. Else if random number is 7:
    elif randNum == 7:
        # 8.1 assign 'bell' to symbol
        symbol = 'bell'
    # 9. Else if random number is 8:
    elif randNum == 8:
        # 9.1 assign 'jackpot' to symbol
        symbol = 'jackpot'
    # 10. return symbol string
    return symbol

def find_winnings(slot1, slot2, slot3, bet):
    # 1. initialize won flag to False
    didWin = False
    # 2. if slot1 equals slot2 and slot2 equals slot3 and slot1 is not 'jackpot' or 'bell':
    if slot1 == slot2 and slot2 == slot3 and slot1 != 'jackpot' and slot1 != 'bell':
        # 2.1 assign amount variable to bet times 3
        amount = bet * 3
        # 2.2 assign result text to 'You got 3 of a kind'
        result = 'You got 3 of a kind.'
        # 2.3 assign won flag to True
        didWin = True
    # 3. else if slot1 equals slot2 or slot2 equals slot3 or slot1 equals slot3:
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        # 3.1 assign amount variable to bet times 2
        amount = bet * 2
        # 3.2 assign result text to 'You got 2 of a kind'
        result = 'You got 3 of a kind.'
        # 3.3 assign won flag to True
        didWin = True
    # 4. else if slot1, slot2, and slot3 are 'bell':
    elif slot1 == 'bell' and slot2 == 'bell' and slot3 == 'bell':
        # 4.1 assign amount variable to bet times 10
        amount = bet * 10
        # 4.2 assign result text to 'You got 3 bells'
        result = 'You got 3 bells.'
        # 4.3 assign won flag to True
        didWin = True
    # 5. else if slot1, slot2, and slot3 are 'jackpot':
    elif slot1 == 'jackpot' and slot2 == 'jackpot' and slot3 == 'jackpot':
        # 5.1 assign amount variable to bet times 20
        amount = bet * 20
        # 5.2 assign result text to 'You got the jackpot!'
        result = 'You got the jackpot!'
        # 5.3 assign won flag to True
        didWin = True
    # 6. else:
    else:
        # 6.1 assign amount variable to bet
        amount = bet
        result = "You didn't get any matches."
    # 7. if won flag is True:
    if didWin:
        # 7.1 assign earnings text to "You won $"
        earnTxt = 'You won $'
    # 8. else:
    else:
        # 8.1 assign earnings text to "You lost your bet of $"
        earnTxt = 'You lost your bet of $'
    # 9. Print result text, earnings text, and amount
    print(result)
    print(earnTxt, amount, '.', sep='')
    # 10. Return amount (will be negative if user lost)
    if didWin == False:
        amount = 0 - amount
    return amount

#  main function
def main():
    #  display introductory message, 'Big Blue Slot Machine!'
    #  call get_name function and assign its return to user's name
    name = get_name()
    #  initialize flag for user can play to True
    canPlay = True
    #  initialize pot to 200
    pot = 200
    #  while user wants to play and pot is not 0 or negative
    while canPlay == True and pot >= 0:
        #  call get_bet function and assign its return to user's bet
        bet = get_bet(pot)
        #  generate random number in range 0 to 8, assign its return to slot1 value
        slot1val = randrange(8)
        #  call translate function, assign its return to slot1 symbol
        slot1sym = translate(slot1val)
        #  generate random number in range 0 to 8, assign its return to slot2 value
        slot2val = randrange(8)
        #  call translate function, assign its return to slot2 symbol
        slot2sym = translate(slot2val)
        #  generate random number in range 0 to 8, assign its return to slot3 value
        slot3val = randrange(8)
        #  call translate function, assign its return to slot3 symbol
        slot3sym = translate(slot3val)
        #  call find_winnings function and add its return to pot amount
        pot += find_winnings(slot1sym, slot2sym, slot3sym, bet)
        #  Report how much is in the pot
        print('You now have $', pot, ' in the pot.', sep='')
        #  if pot amount is greater than 0:
        if pot > 0:
            #  call play_again function, assign its return to user can play flag
            canPlay = play_again()
        #  else: 
        else:
            #  assign user can play flag to False
            canPlay = False
    #  if the pot is less than or equal to 0:
    if pot <= 0:
        #  Output "you are bankrupt"
        print(name, ', you are bankrupt!', sep='')
    #  else:
    else:
        #  Output "you leave with $(pot amount)"
        print(name, ', you leave with $', pot, '.', sep='')
main()