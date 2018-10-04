'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Section: 006
Purpose: Construct a simple slot machine game in a graphics window
Preconditions: player's name (string), bet (integer), whether the user wants to play again (string)
Postconditions: the results of each spin, whether the player won or lost, how much was won or lost, how much is left in the pot
Date: 29 Mar. 2015
'''

# Function: get_name
'''
Purpose: get the name of the player
Preconditions: none
Postconditions: returns the player's name (may have spaces)
'''
# Design:
    # 1. Input the player's name
    # 2. return the player's name

# Function: play_again
'''
Purpose: ask the user if they want to play the game again. 
Preconditions: none
Postconditions: returns True if the user entered y or Y, False if user enters n or N, otherwise returns error message and requests another input.
'''
# Design:
    # 1. input y, Y, n, or N
    # 2. while input is not equal to y, Y, n, or N:
         # 2.1 output "Enter Y, y, N, or n"
         # 2.2 input y, Y, n, or N
    # 3. if input is equal to y or Y:
         # 3.1 Assign True to user wants to play variable
    # 4. else:
         # 3.2 Assign False to user wants to play variable
    # 5. Return user wants to play variable

# Function: get_bet
'''
Purpose: get the amount of the user's bet and check if it is a valid bet
Preconditions: amount in pot as an int. 
Postconditions: returns the amount of the user's bet
'''
# Design:
    # 1. Input the user's bet
    # 2. while the user's bet is not a positive integer that is less than the pot:
        # 2.2 if the user's input contains anything that is not a digit:
             # 2.2.1 Output "You must enter a number"
        # 2.3 Elif bet is greater than pot:
            # 2.3.1 Output "That's too much"
        # 2.4 Else if bet is less than or equal to zero:
            # 2.3.1 Output "That's too small"
        # 2.5 Input the user's bet
    # 3. return bet amount

# Function: translate
'''
Purpose: converts a random number that represents a spin and converts it to a string representing the symbol
Preconditions: a random number in the range 0 to 8 as an int
Postconditions: a string representing the symbol
'''
# Design:
    # 1. If random number is 0:
        # 1.1 assign 'apple' to symbol
    # 2. Else if random number is 1:
        # 2.1 assign 'banana' to symbol
    # 3. Else if random number is 2:
        # 3.1 assign 'cherry' to symbol
    # 4. Else if random number is 3:
        # 4.1 assign 'grapes' to symbol
    # 5. Else if random number is 4:
        # 5.1 assign 'lemon' to symbol
    # 6. Else if random number is 5:
        # 6.1 assign 'melon' to symbol
    # 7. Else if random number is 6:
        # 7.1 assign 'orange' to symbol
    # 8. Else if random number is 7:
        # 8.1 assign 'bell' to symbol
    # 9. Else if random number is 8:
        # 9.1 assign 'jackpot' to symbol
    # 10. return symbol string

# Function: find_winnings
'''
Purpose: determine how much the player won or lost
Preconditions: the results of the spin of each of the 3 wheels, the amount of the bet (to calculate how much the player won or lost). 
Postconditions: returns the amount won or lost and the results of the spins of the 3 wheels.
'''
# Design:
    # 1. initialize won flag to False
    # 2. if all 3 slots are the jackpot:
        # 2.1 assign amount to bet times 20
        # 2.2 assign won flag to True
        # 2.3 assign result text to 'You got the jackpot!'
    # 3. else if all 3 slots are the bell:
        # 3.1 assign amount to bet times 10
        # 3.2 assign won flag to True
        # 3.3 assign result text to 'You got 3 bells.'
    # 4. else if spin is 3 of a kind but not jackpot or bell:
        # 4.1 assign amount to bet times 3
        # 4.2 assign won flag to True
        # 4.3 assign result text to 'You got 3 of a kind.'
    # 5. else if spin is 2 of a kind':
        # 5.1 assign amount to bet times 2
        # 5.2 assign won flag to True
        # 5.3 assign result text to 'You got 2 of a kind.'
    # 6. else:
        # 6.1 assign amount to negative bet
    # 7. if won flag is True:
        # 7.1 assign win or lose text to "You won $"
    # 8. else:
        # 8.1 assign win or lose text to "You lost your bet of $"
    # 9. return result text, win or lose text, and amount

#  main function
    #  display introductory message, 'Big Blue Slot Machine!'
    #  call get_name function and assign its return to user's name
    #  initialize flag for user wants to play to True
    #  initialize pot to 200
    #  while user wants to play and pot is not 0 or negative:
        #  call get_bet function and assign its return to user's bet
        #  display 'Pull the lever! (press Enter)'
        #  generate random number in range 0 to 8 and send it to the translate function for slot1
        #  generate random number in range 0 to 8 and send it to the translate function for slot2
        #  generate random number in range 0 to 8 and send it to the translate function for slot3
        #  call find_winnings function and add its return to pot amount
        #  if pot amount is greater than 0:
            #  call play_again function, assign its return to user wants to play flag
        #  else: 
            #  assign user wants to play flag to False
    #  if the pot is less than or equal to 0:
        #  Output "you are bankrupt"
    #  else:
        #  Output "you leave with $(pot amount)"