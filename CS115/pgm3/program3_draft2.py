'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Section: 006
Purpose: Construct a simple slot machine game in a graphics window
Preconditions: player's name (string), bet (integer), whether the user wants to play again (string)
Postconditions: the results of each spin, whether the player won or lost, how much was won or lost, how much is left in the pot
Date: 02 Apr. 2015
'''
# import graphics to construct the interface
from graphics import *
# import pseudorandom number generator to determine slot machine behavior
from random import randrange
# import sleep function from time library to allow for animation
from time import sleep
#  main function
def main():
    #  display introductory message, 'Big Blue Slot Machine!'
    win = GraphWin('One-Armed Bandit', 950, 700)
    intro = Text(Point(475,100), 'Big Blue Slot Machine!')
    intro.setSize(30)
    intro.setStyle('bold')
    intro.setFill('grey')
    machine = Rectangle(Point(150,50),Point(800,675))
    machine.setWidth(4)
    machine.setOutline('grey')
    machine.setFill('medium blue')
    machine.draw(win)
    lever = Polygon(Point(800,440), Point(890,440), Point(890,250), Point(860,250), Point(860,410), Point(800,410))
    lever.setFill('grey')
    lever.draw(win)
    handle = Circle(Point(875,225), 30)
    handle.setFill('red3')
    handle.draw(win)
    txtBox = Rectangle(Point(200,150), Point(750,400))
    txtBox.setWidth(4)
    txtBox.setOutline('red3')
    txtBox.setFill('white')
    txtBox.draw(win)
    slot1box = Rectangle(Point(199,449), Point(351,601))
    slot1box.setFill('white')
    slot1box.draw(win)
    slot2box = Rectangle(Point(399,449), Point(551,601))
    slot2box.setFill('white')
    slot2box.draw(win)
    slot3box = Rectangle(Point(599,449), Point(751,601))
    slot3box.setFill('white')
    slot3box.draw(win)
    slot1final = Point(275,525)
    slot1final.setFill('white')
    slot1final.draw(win)
    slot2final = Point(475,525)
    slot2final.setFill('white')
    slot2final.draw(win)
    slot3final = Point(275,525)
    slot3final.setFill('white')
    slot3final.draw(win)
    intro.draw(win)   
    #  call get_name function and assign its return to user's name
    name = get_name(win)
    #  initialize flag for user wants to play to True
    wantsPlay = True # assumes user wants to play at least one round
    #  initialize pot to 200
    pot = 200
    potTxt = Text(Point(475,375), 'Pot = $' + str(pot))
    potTxt.setSize(20)
    potTxt.draw(win)
    #  while user wants to play and pot is greater than 0:
    while wantsPlay and pot > 0:
        #  call get_bet function and assign its return to user's bet
        bet = get_bet(pot, win)
        #  generate random number in range 0 to 8 and send it to the translate function for slot1
        slot1sym = translate(randrange(9))
        #  generate random number in range 0 to 8 and send it to the translate function for slot2
        slot2sym = translate(randrange(9))
        #  generate random number in range 0 to 8 and send it to the translate function for slot3
        slot3sym = translate(randrange(9))
        slot1final.undraw() # reset the slots
        slot2final.undraw()
        slot3final.undraw()
        for i in range(10): #  animation for the spinning wheels
            slot1rand = translate(randrange(9))
            slot1gif = Image(Point(275,525), slot1rand + '.gif')
            slot1gif.draw(win)
            slot2rand = translate(randrange(9))
            slot2gif = Image(Point(475,525), slot2rand + '.gif')
            slot2gif.draw(win)
            slot3rand = translate(randrange(9))
            slot3gif = Image(Point(675,525), slot3rand + '.gif')
            slot3gif.draw(win)
            sleep(0.1)
            slot1gif.undraw()
            slot2gif.undraw()
            slot3gif.undraw()
        # draw the results of the spin
        slot1final = Image(Point(275,525), slot1sym + '.gif')
        slot2final = Image(Point(475,525), slot2sym + '.gif')
        slot3final = Image(Point(675,525), slot3sym + '.gif')
        slot1final.draw(win)
        slot2final.draw(win)
        slot3final.draw(win)
        #  call find_winnings function and add its return to pot amount
        pot += find_winnings(slot1sym, slot2sym, slot3sym, bet, win)
        # update the pot amount
        potTxt.setText('Pot = $' + str(pot))
        #  if pot amount is greater than 0:
        if pot > 0:
            #  call play_again function, assign its return to user wants to play flag
            wantsPlay = play_again(win)
    
    # if pot is less than 0:
    if pot < 0:
        # Output "you are bankrupt"
        resultTxt = Text(Point(475,275), name + ', you are bankrupt!')
        resultTxt.setFill('red3')
    #  else:
    else:
        #  Output "you leave with $(pot amount)"
        resultTxt = Text(Point(475,275), name + ', you leave with $' + str(pot))
        resultTxt.setFill('mediumblue')
    resultTxt.setSize(20)
    resultTxt.draw(win)
    clickTxt = Text(Point(475, 325), '(Click to exit)')
    clickTxt.setSize(15)
    clickTxt.draw(win)
    win.getMouse()
    win.close()
        
# Function: get_name
def get_name(window):
    '''
    Purpose: get the name of the player
    Preconditions: name of the graphics window, inputs player's name from entry box
    Postconditions: returns the player's name as a string, undraw graphics objects
    '''
    # Design:
    # 1. Input the player's name and return it
    namePrompt = Text(Point(475,200), "What's your name?")
    namePrompt.setSize(15)
    namePrompt.draw(window)
    nameBox = Entry(Point(475,250), 10)
    nameBox.setText('Name')
    nameBox.draw(window)
    clickTxt = Text(Point(475, 300), '(Click to continue)')
    clickTxt.setSize(15)
    clickTxt.draw(window)
    window.getMouse()
    name = nameBox.getText()
    namePrompt.undraw()
    nameBox.undraw()
    clickTxt.undraw()
    return name

# Function: play_again
def play_again(window):
    '''
    Purpose: ask the user if they want to play the game again. 
    Preconditions: requires the user to click one of two buttons
    Postconditions: returns True if the user clicks 'yes' button, False if user clicks 'no' button, otherwise requests another input. undraws graphics objects
    '''
    # Design:
    playAgainTxt = Text(Point(475, 180), 'Do you want to play again?')
    playAgainTxt.setSize(15)
    playAgainTxt.draw(window)
    yesBtn = Rectangle(Point(415, 260), Point(455,290))
    yesBtn.setFill('dark green')
    yesBtn.draw(window)        
    yesTxt = Text(Point(435, 275), 'YES')
    yesTxt.setFill('grey90')
    yesTxt.draw(window)
    noBtn = Rectangle(Point(495,260), Point(535,290))
    noBtn.setFill('red3')
    noBtn.draw(window)
    noTxt = Text(Point(515,275), 'NO')
    noTxt.setFill('grey90')
    noTxt.draw(window)   
    # Initialize sentinel
    inputIsValid = False
    click = window.getMouse()
    # While user doesn't click one of the buttons:
    while not inputIsValid:        
        xCoord = click.getX()
        yCoord = click.getY()
        #  if user clicks yes button:
        if xCoord >= 415 and xCoord <= 455 and yCoord >= 260 and yCoord <= 290:
            yesBtn.setFill('grey')
            sleep(.2)
            yesBtn.setFill('dark green')
            #  assign True to play again variable
            wantsToPlay = True
            #  assign True to valid input flag to end the while loop
            inputIsValid = True          
        #  else if user clicks no button':
        elif xCoord >= 495 and xCoord <= 535 and yCoord >= 260 and yCoord <= 290:
            noBtn.setFill('grey')
            sleep(.2)
            yesBtn.setFill('red3')
            #  assign False to play again variable
            wantsToPlay = False
            #  assign True to valid input flag to end the while loop
            inputIsValid = True
        else:
            #  Get a click from the user
            click = window.getMouse()            
    playAgainTxt.undraw()
    yesTxt.undraw()
    noTxt.undraw()
    yesBtn.undraw()
    noBtn.undraw()
    #  return play again variable
    return wantsToPlay

# Function: get_bet
def get_bet(pot,window):
    '''
    Purpose: get the amount of the user's bet and verify that it's a positive integer
    Preconditions: amount in pot as an int, name of the graphics window, inputs bet from entry box
    Postconditions: returns the amount of the user's bet, undraws graphics objects
    '''
    # Input the user's bet
    betPrompt = Text(Point(475, 180), 'How much do you want to bet? (up to $' + str(pot) + ')')
    betPrompt.setSize(15)
    betPrompt.draw(window)
    betBox = Entry(Point(475, 220), 10)
    betBox.setText('50')
    betBox.draw(window)
    goTxt = Text(Point(475, 260), 'Pull the lever!')
    goTxt.setSize(15)
    goTxt.draw(window)
    
    window.getMouse()
    isValid = False # Initialize sentinel
    # while the user's bet is not a positive integer that is less than the pot:
    while not isValid:
        bet = betBox.getText()
        # if the user's input contains anything that is not a digit:
        if not bet.isdigit():
            feedback = Text(Point(475,300),'Enter a positive integer -- no letters!')
        # else if the user's input is larger than the pot:
        elif int(bet) > pot:
            feedback = Text(Point(475,300),"You can't bet that much!")
        # else if the user's input is zero or less:
        elif int(bet) <= 0:
            feedback = Text(Point(475,300),'You have to bet more than that!')
        # else: (if the bet is valid)
        else:
            isValid = True
        # get another click if the bet is not valid
        if not isValid:
            feedback.setFill('red3')
            feedback.setSize(15)            
            feedback.draw(window)
            window.getMouse()
            feedback.undraw()
    betPrompt.undraw()
    betBox.undraw()
    goTxt.undraw()
    validBet = int(bet)
    # return validated bet
    return validBet

def translate(randNum):
    '''
    Purpose: converts a positive integer to a string representing the symbol of the slot
    Preconditions: a random number in the range 0 to 8 as an int
    Postconditions: a string representing the symbol of the slot
    '''
    # 1. If random number is 0:
    if randNum == 0:
        # 1.1 assign 'bell' to symbol
        symbol = 'bell'
    # 2. Else if random number is 1:
    elif randNum == 1:
        # 2.1 assign 'apple' to symbol
        symbol = 'apple'
    # 3. Else if random number is 2:
    elif randNum == 2:
        # 3.1 assign 'banana' to symbol
        symbol = 'banana'
    # 4. Else if random number is 3:
    elif randNum == 3:
        # 4.1 assign 'orange' to symbol
        symbol = 'orange'
    # 5. Else if random number is 4:
    elif randNum == 4:
        # 5.1 assign 'cherry' to symbol
        symbol = 'cherry'
    # 6. Else if random number is 5:
    elif randNum == 5:
        # 6.1 assign 'grapes' to symbol
        symbol = 'grapes'
    # 7. Else if random number is 6:
    elif randNum == 6:
        # 7.1 assign 'jackpot' to symbol
        symbol = 'jackpot'
    # 8. Else if random number is 7:
    elif randNum == 7:
        # 8.1 assign 'lemon' to symbol
        symbol = 'lemon'
    # 9. Else if random number is 8:
    elif randNum == 8:
        # 9.1 assign 'melon' to symbol
        symbol = 'melon'
    # 10. return symbol string
    return symbol    

# Function: find_winnings
def find_winnings(slot1, slot2, slot3, bet, window):
    '''
    Purpose: determine how much the player won or lost
    Preconditions: the results of the spin of each of the 3 wheels, the amount of the bet as an int 
    Postconditions: returns the amount won or lost and the results of the spins of the 3 wheels.
    '''
    #  if slot1, slot2, and slot3 are 'jackpot':
    if slot1 == slot2 == slot3 == 'jackpot':
        #  assign amount variable to bet times 20
        amount = bet * 20
        #  assign result text to 'You got the jackpot!'
        result = 'You got the jackpot!'
            #  assign won flag to True
        didWin = True
    #  else if slot1, slot2, and slot3 are 'bell':
    elif slot1 == slot2 == slot3 == 'bell':
        #  assign amount variable to bet times 10
        amount = bet * 10
        #  assign result text to 'You got 3 bells'
        result = 'You got 3 bells.'
        #  assign won flag to True
        didWin = True    
    # else if spin is 3 of a kind but not 'jackpot' or 'bell':
    elif slot1 == slot2 == slot3:
        #  assign amount variable to bet times 3
        amount = bet * 3
        #  assign result text to 'You got 3 of a kind'
        result = 'You got 3 of a kind.'
        #  assign won flag to True
        didWin = True 
    elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        #  assign amount variable to bet times 2
        amount = bet * 2
        #  assign result text to 'You got 2 of a kind'
        result = 'You got 2 of a kind.'
        #  assign won flag to True
        didWin = True   
    #  else:
    else:
        #  assign amount variable to bet
        amount = bet
        result = "You didn't get any matches."
        # assign won flag to False
        didWin = False
    #  if won flag is True:
    if didWin:
        #  assign won/lost text to "You won $"
        won_or_lost = 'You won $'
    #  else:
    else:
        #  assign won/lost text to "You lost your bet of $"
        won_or_lost = 'You lost your bet of $'
    #  Output result text, earnings text, and amount
    resultTxt = Text(Point(475, 180), result)
    resultTxt.setSize(15)
    resultTxt.draw(window)
    earnTxt = Text(Point(475, 220), won_or_lost + str(amount) + '.')
    earnTxt.setSize(15)
    earnTxt.draw(window)
    clickTxt = Text(Point(475, 275), "(Click to continue)")
    clickTxt.setSize(15)
    clickTxt.draw(window)
    window.getMouse()
    resultTxt.undraw()
    earnTxt.undraw()
    clickTxt.undraw()
    #  Return amount (will be negative if user lost)
    if not didWin:
        amount = -amount
    return amount
    
main()