#Suppose there is a game for 2 players
#Each player can choose a number from 1 and 2 to add from 0
#The first player to make the total number greater than 10 will win the game
#The level 0 player will forever add 2
#Suppose the player 1 is in level 1, player 2 is in level 2
#Suppose every one wants to win the game at quick as he/she can
 
  
#The strategy of player 1 is to make sure the total number before he add to be 9 or 10
#So he/she should add the total number to 7 or 8
#also, if the number he receive is 8 he will lose
#so he shouldn't add the total number to 6
#which means if the number he receive is 4, he will add 1 instead of 2
def p1strategy(totalNumber):
    if totalNumber == 4:
        totalNumber += 1
    elif totalNumber <7 or totalNumber == 9 :
        totalNumber+=2
    else:
        totalNumber+=1 
    return totalNumber
def p2strategy(totalNumber):   
    #Player2 knows player1's strategy, so he/she will add the number to 8 or 5 or 2 or 1
    if totalNumber <= 1:
        totalNumber += 1
    elif totalNumber<=3:
        totalNumber += 2
    elif totalNumber == 4:
        totalNumber += 1
    elif totalNumber <= 6:
        totalNumber += 2
    elif totalNumber <= 8:
        totalNumber += 1
    else:
        totalNumber += 2
    return totalNumber

def gameFunc(first):
    Sum = 0
    if first == 1:
        while True:
            Sum = p1strategy(Sum)
            print('player1 adds the number, now the total number is {}'.format(Sum))
            if Sum > 10:
                print('player1 wins!')
                break
            Sum = p2strategy(Sum)
            print('player2 adds the number, now the total number is {}'.format(Sum))
            if Sum > 10:
                print('player2 wins!')
                break
        return
    if first == 2:
        while True:
            Sum = p2strategy(Sum)
            print('player2 adds the number, now the total number is {}'.format(Sum))
            if Sum > 10:
                print('player2 wins!')
                break
            Sum = p1strategy(Sum)
            print('player1 adds the number, now the total number is {}'.format(Sum))
            if Sum > 10:
                print('player1 wins!')
                break
        return

gameFunc(2)
        
        
            

    
