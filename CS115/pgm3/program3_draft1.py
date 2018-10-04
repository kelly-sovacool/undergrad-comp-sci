'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Section: 006
Purpose: Construct a simple slot machine game in a graphics window
Preconditions: player's name (string), bet (integer), whether the user wants to play again (string)
Postconditions: the results of each spin, whether the player won or lost, how much was won or lost, how much is left in the pot
Date:
'''
# Import randrange function from random library to generate slot spins
from random import randrange
# Import graphics library to construct the user interface
from graphics import *
# Import sleep function from time library to allow for animation
from time import sleep

def get_name(window):
    '''
    Purpose:
    Preconditions:
    Postconditions:
    '''
    # 1. Input the player's name
    namePrompt = Text(Point(200,100), "What's your name?")
    namePrompt.setSize(15)
    namePrompt.draw(window)
    nameBox = Entry(Point(310,100), 10)
    nameBox.setText('Name')
    nameBox.draw(window)
    clickTxt = Text(Point(250, 130), '(Click to continue)')
    clickTxt.setSize(15)
    clickTxt.draw(window)
    window.getMouse()
    name = nameBox.getText()
    # 2. return the player's name
    namePrompt.undraw()
    nameBox.undraw()
    clickTxt.undraw()
    return name

def play_again(window):
    '''
    Purpose:
    Preconditions:
    Postconditions:
    '''
    playAgainTxt = Text(Point(250, 130), 'Do you want to play again?')
    playAgainTxt.setSize(15)
    playAgainTxt.draw(window)
    yesBtn = Rectangle(Point(190, 150), Point(230,170))
    yesBtn.setFill('dark green')
    yesBtn.draw(window)        
    yesTxt = Text(Point(210, 160), 'YES')
    yesTxt.setFill('grey90')
    yesTxt.draw(window)
    noBtn = Rectangle(Point(270,150), Point(310,170))
    noBtn.setFill('red3')
    noBtn.draw(window)
    noTxt = Text(Point(290,160), 'NO')
    noTxt.setFill('grey90')
    noTxt.draw(window)    
    # . Initialize flag for valid input as False
    isInputValid = False
    # . while flag for valid input is False:
    while isInputValid == False:
        #  Wait for user to click a button
        click = window.getMouse()
        xCoord = click.getX()
        yCoord = click.getY()
        #  if user clicks yes button:
        if xCoord >= 190 and xCoord <= 230 and yCoord >= 150 and yCoord <= 170:
            yesBtn.setFill('grey')
            sleep(.2)
            yesBtn.setFill('dark green')
            #  assign True to play again variable
            wantsToPlayAgain = True
            #  assign True to valid input flag to end the while loop
            isInputValid = True          
        #  else if user clicks no button':
        elif xCoord >= 270 and xCoord <= 310 and yCoord >= 150 and yCoord <= 170:
            noBtn.setFill('grey')
            sleep(.2)
            yesBtn.setFill('red3')
            #  assign False to play again variable
            wantsToPlayAgain = False
            #  assign True to valid input flag to end the while loop
            isInputValid = True           
    #  return play again variable
    playAgainTxt.undraw()
    yesTxt.undraw()
    noTxt.undraw()
    yesBtn.undraw()
    noBtn.undraw()
    return wantsToPlayAgain

def get_bet(pot, window):
    '''
    Purpose:
    Preconditions:
    Postconditions:
    '''
    # Construct the graphics objects for how much the user wants to bet
    betPrompt = Text(Point(250, 100), 'How much do you want to bet? (up to $' + str(pot) + ')')
    betPrompt.setSize(15)
    betPrompt.draw(window)
    betBox = Entry(Point(250, 125), 10)
    betBox.setText('1')
    betBox.draw(window)
    goTxt = Text(Point(250, 150), 'Pull the lever!')
    goTxt.setSize(15)
    goTxt.draw(window)
    arrow = Polygon(Point(300,147), Point(300,153), Point(385,153), Point(385,157), Point(395,150), Point(385,143), Point(385,147))
    arrow.setFill('red3')
    arrow.draw(window)
    #  Initialize flag for valid bet to False
    isBetValid = False
    #  while valid bet flag is False:
    while isBetValid == False:
        #  input the amount of the user's bet when the user clicks the lever
        pulledLever = False
        while pulledLever == False:
            click = window.getMouse()
            xClick = click.getX()
            yClick = click.getY()
            if xClick >= 435 and xClick <= 485 and yClick >= 45 and yClick <= 270:
                pulledLever = True # ends the loop if user clicks the lever
            else:
                arrow.setFill('grey')
                sleep(.2) # make the arrow flash grey
                arrow.setFill('red3')
        bet = float(betBox.getText())
        # If bet is not an integer
        if bet % 1 != 0:
            #  Output "We don't use change: please bet a whole number."
            intTxt = Text(Point(250,190), "We don't use change: bet a whole number.")
            intTxt.setSize(15)
            intTxt.draw(window)
            sleep(3)
            intTxt.undraw()
        #  If bet is greater than pot:
        elif bet > pot:
            #  Output "That's too much"
            tooBigTxt = Text(Point(250,190), "You can't bet that much!")
            tooBigTxt.setSize(15)
            tooBigTxt.draw(window)
            sleep(3) # Pause long enough for user to read it before undrawing
            tooBigTxt.undraw()
        #  Else if bet is less than or equal to zero:
        elif bet <= 0:
            #  Output "That's too small"
            tooLilTxt = Text(Point(250,190), "You have to bet more than that!")
            tooLilTxt.setSize(15)
            tooLilTxt.draw(window)
            sleep(3) # Pause long enough for user to read it before undrawing
            tooBigTxt.undraw()
        #  Else:
        else:
            #  assign True to valid bet flag: ends the loop
            isBetValid = True
    
    for i in range(80,67,-4): # animate the coin entering the slot
        movingCoin = Circle(Point(i, 145), 15)
        movingCoin.setFill('gold')
        movingCoin.setOutline('goldenrod')
        movingSign = Text(Point(i, 145), '$')
        movingSign.setFill('goldenrod')
        movingCoin.draw(window)
        movingSign.draw(window)
        movingSign.undraw()
        movingCoin.undraw()
    bet = int(bet)
    betPrompt.undraw()
    betBox.undraw()
    goTxt.undraw()
    arrow.undraw()
    # 3. return bet amount
    return bet

def translate(randNum):
    '''
    Purpose:
    Preconditions:
    Postconditions:
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
    
def find_winnings(slot1, slot2, slot3, bet, window):
    '''
    Purpose:
    Preconditions:
    Postconditions:
    '''
    # 1. initialize won flag to False
    didWin = False
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
        #  assign amount variable to negative bet
        amount = -bet
        result = "You didn't get any matches."
    #  if won flag is True:
    if didWin:
        #  assign earnings text to "You won $"
        earnings = 'You won $'
    #  else:
    else:
        #  assign earnings text to "You lost your bet of $"
        earnings = 'You lost your bet of $'
    #  Output result text, earnings text, and amount
    resultTxt = Text(Point(250, 100), result)
    resultTxt.setSize(15)
    resultTxt.draw(window)
    earnTxt = Text(Point(250, 125), earnings + str(amount) + '.')
    earnTxt.setSize(15)
    earnTxt.draw(window)
    clickTxt = Text(Point(250, 150), "(Click to continue)")
    clickTxt.setSize(15)
    clickTxt.draw(window)
    window.getMouse()
    #  Return amount (will be negative if user lost)
    resultTxt.undraw()
    earnTxt.undraw()
    clickTxt.undraw()
    return amount

def animate(slot_sym, slot_num, window):
    '''
    Purpose: Animate the spinning wheels of the slot machine in the graphics window
    Preconditions: symbol of the slot (string), slot number (int), and the graphics window name
    Postconditions: 
    '''
    slot_holder = Rectangle(Point(15 + (slot_num - 1) * 150,275), Point(185 + (slot_num - 1) * 150,425))
    slot_holder.setFill('white')
    slot_holder.draw(window)
    for i in range(10): # animates the spinning wheels
        rand_sym = translate(randrange(9))
        moving_gif = Image(Point(95 + (slot_num - 1) * 150, 350), rand_sym + '.gif')
        moving_gif.draw(window)
        sleep(0.1)
        moving_gif.undraw()
    slot_final_gif = Image(Point(95 + (slot_num - 1) * 150, 350), slot_sym + '.gif')
    slot_final_gif.draw(window)
    slot_txt_box = Rectangle(Point(105 + (slot_num - 1) * 125, 230), Point(145 + (slot_num - 1) * 125, 244))
    slot_txt_box.setFill('white')
    slot_txt_box.draw(window)
    slot_txt = Text(Point(125 + (slot_num - 1) * 125, 237), slot_sym)
    slot_txt.draw(window)

def money_draw(pot, window):
    '''
    Purpose: Construct graphics objects representing money given the amount in the pot
    Preconditions: amount in pot as positive integer
    Postconditions: returns none; draws circles to represent money
    '''
    block = Rectangle(Point(35,425), Point(465,465))
    block.setFill('medium blue')
    block.setOutline('medium blue')
    block.draw(window)
    if pot > 0: # Draws coins to represent money in the pot
        for i in range(0,pot + 1, 10):
            xloc = randrange(50,446)
            yloc = randrange(445,450)
            coin = Circle(Point(xloc, yloc), 15)
            coin.setFill('gold')
            coin.setOutline('goldenrod')
            coin.draw(window)
            sign = Text(Point(xloc, yloc), '$')
            sign.setFill('goldenrod')
            sign.draw(window)

#  main function
def main():
    win = GraphWin('One-Armed Bandit', 500, 500)
    #  display introductory message, 'Big Blue Slot Machine!'
    intro = Text(Point(250,60), 'Big Blue Slot Machine!')
    intro.setSize(20)
    intro.setStyle('bold')
    intro.setFill('blue')
    machine = Rectangle(Point(10, 25),Point(490,490))
    machine.setWidth(4)
    machine.setOutline('grey')
    machine.setFill('medium blue')
    machine.draw(win)
    lever = Polygon(Point(450,50), Point(470,50), Point(470,270), Point(450,270), Point(430,270), Point(430,250), Point(450,250))
    lever.setFill('grey')
    lever.draw(win)
    handle = Circle(Point(460,70), 25)
    handle.setFill('red3')
    handle.draw(win)
    txtBox = Rectangle(Point(100,40), Point(400,250))
    txtBox.setWidth(4)
    txtBox.setOutline('red3')
    txtBox.setFill('white')
    txtBox.draw(win)
    intro.draw(win)
    slots = Rectangle(Point(15,275), Point(485,425))
    slots.setFill('white')
    slots.draw(win)
    line1 = Line(Point(178,275), Point(178,425))
    line1.draw(win)
    line2 = Line(Point(322,275), Point(322,425))
    line2.draw(win)
    for i in range(3):
        slot_txt_box = Rectangle(Point(105 + i * 125, 230), Point(145 + i * 125, 244))
        slot_txt_box.setFill('white')
        slot_txt_box.draw(win)
    moneyTray = Polygon(Point(20,440), Point(20,475), Point(480,475), Point(480,440), Point(465,460), Point(465,465), Point(35,465), Point(35,460))
    moneyTray.setFill('grey')
    moneyTray.draw(win)
    hole = Rectangle(Point(50,125), Point(60,165))
    hole.setFill('black')
    hole.draw(win)
    
    #  call get_name function and assign its return to user's name
    name = get_name(win)
    #  initialize flag for user can play to True
    canPlay = True
    #  initialize pot to 200
    pot = 200
    money_draw(pot, win)
    #  while user wants to play and pot is not 0 or negative
    while canPlay == True and pot >= 0:
        potTxt = Text(Point(150,215), 'Pot: $' + str(pot))
        potTxt.setSize(17)
        potTxt.setFill('dark green')
        potTxt.draw(win)
        #  call get_bet function and assign its return to user's bet
        bet = get_bet(pot, win)
        #  generate random number in range 0 to 8, assign its return to slot1 value
        slot1val = randrange(9)
        #  call translate function, assign its return to slot1 symbol
        slot1sym = translate(slot1val)
        animate(slot1sym, 1, win)
        #  generate random number in range 0 to 8, assign its return to slot2 value
        slot2val = randrange(9)
        #  call translate function, assign its return to slot2 symbol
        slot2sym = translate(slot2val)
        animate(slot2sym, 2, win)
        #  generate random number in range 0 to 8, assign its return to slot3 value
        slot3val = randrange(9)
        #  call translate function, assign its return to slot3 symbol
        slot3sym = translate(slot3val)
        animate(slot3sym, 3, win)
        #  call find_winnings function and add its return to pot amount
        pot += find_winnings(slot1sym, slot2sym, slot3sym, bet, win)
        money_draw(pot, win)
        #  Report how much is in the pot
        potRep = Text(Point(250, 100), 'You now have $' + str(pot) + ' in the pot.')
        potRep.setSize(15)
        potRep.draw(win)
        potTxt.undraw()
        #  if pot amount is greater than 0:
        if pot > 0:
            #  call play_again function, assign its return to user can play flag
            canPlay = play_again(win)
        #  else: 
        else:
            #  assign user can play flag to False
            canPlay = False
        potRep.undraw()

    #  if the pot is less than or equal to 0:
    if pot <= 0:
        #  Output "you are bankrupt"
        bankTxt = Text(Point(250,150), name + ', you are bankrupt!')
        bankTxt.setFill('red3')
        bankTxt.setSize(20)
        bankTxt.draw(win)
    #  else:
    else:
        #  Output "you leave with $(pot amount)"
        amtTxt = Text(Point(250,150), name + ', you leave with $' + str(pot) + '.')
        amtTxt.setFill('medium blue')
        amtTxt.setSize(20)
        amtTxt.draw(win)
    clickEndTxt = Text(Point(250, 200), "(Click to exit)")
    clickEndTxt.setSize(15)
    clickEndTxt.draw(win)
    win.getMouse()
    win.close()
main()