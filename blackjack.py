import random

def interface():
    flag = 0
    #starting interface that will either start game or end game
    while(flag!=1):
        print('##########BLACKJACK GAME##########')
        print('1. Start Game')
        print('2. Exit')
        try:
            choose = int(input('Enter your choice'))
            print(choose)
            flag = 1
        except ValueError:
            print('Error fuck face')
    if choose == 1:
        startGame()
    else:
        print('Thank You for playing')
        exit

def startGame():
    player = random.randint(1,10) + random.randint(1,10)
    dealer = random.randint(1,10)
    print('Player Cardvalue: ' + str(player))
    print('Dealer Cardvalue: ' + str(dealer))
    PlayGame(player,dealer)
    

def update_value(x):
    return x + random.randint(0,10)



def PlayGame(player, dealer):
        print('1. To hit player')
        print('2. To hit Dealer')
        try:
            choice = int(input('Make a choice'))
            if choice == 1:
                player = update_value(player)
                print('Player value = ' + str(player))
            elif choice == 2 and dealer <=16:
                dealer = update_value(dealer)
                print('Dealer value = ' + str(dealer))
            else:
                print('Wrong Choice Mofo')
            if player == 21:
                print('BlackJack! You win')
                exit
            elif dealer == 21:
                print('BlackJack! Dealer Won!')
                exit
            elif player>21:
                print('You lost')
                exit
            elif dealer>21:
                print('You win')
                exit
            else:
                PlayGame(player,dealer)
        except ValueError:
            print('Wrong input')
            PlayGame(player,dealer)
                

interface()
