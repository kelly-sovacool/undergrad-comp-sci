# Program 2 Functions design

# Function: getname
# Purpose: get the name of the player
# Preconditions: none
# Postconditions: returns the player's name (may have spaces)
# Design:
    # Input the player's name
    # return the player's name

# Function: play_again
# Purpose: ask the user if they want to play the game again. 
# Preconditions: none
# Postconditions: returns True if the user entered y or Y, False if user enters n or N, otherwise returns error message and requests another input.
# Design:
    # Initialize flag for valid input as False
    # while flag for valid input is False:
        # Input y, Y, n, or N
        # if input is y or Y:
            # assign True to play again variable
            # assign True to valid input flag           
        # else if input is n or N:
            # 2.3.2 assign False to play again variable
            # 2.3.1 assign True to valid input flag
    # return play again variable

# Function: get_bet
# Purpose: get the amount of the user's bet and check if it is a valid bet
# Preconditions: amount in pot as an int. 
# Postconditions: returns the amount of the user's bet
# Design:
    # Initialize flag for valid bet to False
    # while valid bet flag is False:
        # input the amount of the user's bet
        # If bet is greater than pot:
            # Output "That's too much"
        # Else if bet is less than or equal to zero:
            # Output "That's too small"
        # Else:
            # assign True to valid bet flag
    # return bet amount

# Function: translate
# Purpose: converts a random number that represents a spin and converts it to a string representing the symbol
# Preconditions: a random number in the range 0 to 8 as an int
# Postconditions: a string representing the symbol
# Design:
    # If random number is 0:
        # assign 'apple' to symbol
    # Else if random number is 1:
        # assign 'banana' to symbol
    # Else if random number is 2:
        # assign 'cherry' to symbol
    # Else if random number is 3:
        # assign 'grapes' to symbol
    # Else if random number is 4:
        # assign 'lemon' to symbol
    # Else if random number is 5:
        # assign 'melon' to symbol
    # Else if random number is 6:
        # assign 'orange' to symbol
    # Else if random number is 7:
        # assign 'bell' to symbol
    # Else if random number is 8:
        # assign 'jackpot' to symbol
    # return symbol string

# Function: find_winnings
# Purpose: determine how much the player won or lost
# Preconditions: the results of the spin of each of the 3 wheels, the amount of the bet (to calculate how much the player won or lost). 
# Postconditions: returns the amount won or lost, the results of the spins of the 3 wheels.
# Design:
    # initialize won flag to False
    # if slot1 equals slot2 and slot2 equals slot3 and slot1 is not 'jackpot' or 'bell':
        # assign amount to bet times 3
        # assign won flag to True
    # else if slot1 equals slot2 or slot2 equals slot3 or slot1 equals slot3:
        # assign amount to bet times 2
        # assign won flag to True
    # else if slot1, slot2, and slot3 are 'bell':
        # assign amount to bet times 10
        # assign won flag to True
    # else if slot1, slot2, and slot3 are 'jackpot':
        # assign amount to bet times 20
        # assign won flag to True
    # else:
        # assign amount to bet
    # if won flag is True:
        # assign output text to "You won $"
    # else:
        # assign output text to "You lost your bet of $"
    # return output text and amount