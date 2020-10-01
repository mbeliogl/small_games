from playingcards import *

def main():
    deck = Deck()
    deck.shuffle()
    deck.cut()
    userPoints = 0
    comPoints = 0
    while len(deck) > 0 :
        input('Hit Enter To Pick A Card Please ')
        userCard = deck.takeTop()
        cCard = deck.takeTop()
        print('User Card is: ', userCard)
        print('Computer Card is: ', cCard)
        
        if userCard > cCard:
            userPoints += 1
        elif cCard > userCard:
            comPoints += 1
        else:
            print('Draw')

        print('User Score: ', userPoints)
        print('Computer Score: ', comPoints)
        
    if userPoints > comPoints:
        print(f'\n-----USER WINS-----')
    elif userPoints == comPoints:
        print(f'\n-----TIE-----')
    else:
        print(f'\n-----COMPUTER WINS-----')
        
main()
