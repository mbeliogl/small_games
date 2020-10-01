
import math
import random

def guessingGame():

    max_num = int(input(f"\nPlease enter the maximum number allowed: "))
    
    gen_number = random.randint(0, max_num)
    play = True #boolean to decide whether to play again 
    win = False #boolean to decide if the player guessed right
    
    while play:
        chance = 1 
        print(f"\nOkay! I'm thinking of a number from 0 to {max_num}. You have 3 guesses!")
        for i in range(3):
            print(f"--Guess {chance}")
            user_input = int(input(f"--Input a number (0 - {max_num}): "))

            if user_input > gen_number:
                print("Woah! Too Big!"+'\n')

            elif user_input < gen_number:
                print("Ehhh! Too Small!"+'\n')

            elif user_input == gen_number:
                print("You Guessed Correct!")
                play_again = input(f"Play again? y/n \n")
                play = playAgain(play_again, play)
            
            chance += 1

        play_again = input(f"You're out of luck! Play again? y/n \n")
        play = playAgain(play_again, play)

#helper method to determine if player wants to try again
def playAgain(play_again, play):            
    if play_again == 'y':
        play = True
        guessingGame()

    if play_again == 'n':   
        play = False
        exit()

    return play



def main():
    guessingGame()

main()
    
