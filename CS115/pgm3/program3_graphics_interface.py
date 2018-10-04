from graphics import *
def main():
    win = GraphWin('One-Armed Bandit', 950, 800)
    #  display introductory message, 'Big Blue Slot Machine!'
    intro = Text(Point(475,100), 'Big Blue Slot Machine!')
    intro.setSize(30)
    intro.setStyle('bold')
    intro.setFill('grey')
    machine = Rectangle(Point(150,50),Point(800,750))
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
    intro.draw(win)
    
    win.getMouse()
    win.close()
    
def play_Again(window):
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

def get_bet(pot, window):
    # Input the user's bet
    betPrompt = Text(Point(475, 180), 'How much do you want to bet? (up to $' + str(pot) + ')')
    betPrompt.setSize(15)
    betPrompt.draw(window)
    betBox = Entry(Point(475, 220), 10)
    #betBox.setText('50')
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
    validBet = int(bet)
    return validBet

main()