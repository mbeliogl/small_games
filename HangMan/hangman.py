
import random

# fills out the 'word'
def getSpots(l, word):
    alist=[]
    for i in range(len(word)):
        if word[i] == l:
           alist = alist + [i]
    return alist
        
# driver function
def main():
    words = ['extracurriculum', 'unescapably', 'increment', 'mario', 'luigi', 'openhanded', 'super', 'shell', 'harvest', 'reputation', 'sonic', 'dispersement', 'tails', 'zelda', 'link', 'sword', 'pacman', 'extra', 'rick', 'conceivably', 'morty', 'agile', 'connection', 'fiddler', 'theologically', 'enrichment', 'primarily', 'primary','diamondium', 'semiterrestrial', 'election', 'marriage', 'eclectic']
    num = random.randint(0, 33)
    word = words[num]
    
    print(f"\nI'm thinking of a word from the dictionary. Can you guess what it is?\n")
    progList = ['_'] * len(word)
   

    for i in range(len(word)):
        print(f"{progList}\n")
        guesses_left = len(word)-i
        print('You Have',len(word)-i, 'Guesses Left\n')
        userInput = input('Please Guess a Letter! (or type "solve" to solve the puzzle): ')


        if userInput == 'solve':
                userinput = input('What do you think the word is? ')
                if userinput == word:
                        print("\n----- That's Right! You Win -----")
                else:
                        print("\n----- That's not right!" + '\n')
                        print('----- The word was: ' + word + '\n')
                        print('----- Please Try Again!')
                break

        elif userInput in word:
                print(f'\nCorrect! That letter is in the word!\n')
                
                spots = getSpots(userInput, word)
                for spot in spots:
                        progList[spot] = userInput
        else:
                print(f"\nWrong! {userInput} is not in the word\n")


        if guesses_left == 1:
        	print("----- You are out of guesses! -----")
        	exit()
main()
