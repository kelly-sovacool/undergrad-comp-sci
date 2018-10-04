# get_bet text version
def get_bet(pot):
    bet = input('Enter your bet: ')
    isValid = False
    while not isValid:
        if not bet.isdigit():
            print('Enter a positive integer -- no letters!')
        elif int(bet) > pot:
            print("You can't bet that much!")
        else:
            isValid = True
        if not isValid:
            bet = input('Enter your bet: ')
    validBet = int(bet)
    print("You bet $",validBet)
get_bet(200)