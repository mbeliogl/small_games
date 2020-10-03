
import random
import sys

def readPlay(inFilename):
    fin = open(inFilename, 'r')
    text = fin.readlines()

    play = []
    currScene = {}

    for line in text:
        line = line.strip('\n')
        if 'ACT' in line:
            currAct = []
            play.append(currAct)
        # same but with SCENE
        elif 'SCENE' in line:
            
            currAct.append(currScene)
        
        # checks if the line is a character name
        elif 'ACT' not in line and 'SCENE' not in line and line == line.upper():
            # removes the dot if it is there
            if '.' in line:
                line = line.strip('.')
            #stores the current char
            currChar = line
            
        #adding current character to keys 
        if currChar not in currScene.keys():
            charLine = []
            currScene[currChar] = charLine
            
        #assinging current line to current scene 
        else:
            currentLine = currScene.get(currChar)
            currentLine.append(line)
            currScene[currChar] = currentLine
           
    return play
'''
Takes a play and a series of indices into that play: an act, scene, character name, and an index into that character's list of lines and prints out a multiple-choice question about which character says that particular line in that particular act and scene. The last parameter is the number of the question. This function returns the letter associated with the correct answer (a, b, c, or d)
'''
def printQuestion(play, actIndex, sceneIndex, characterName, lineIndex, questionNum):
   
    #Print the question
    print("Question " + str(questionNum) + ": In act " + str(actIndex + 1) + ", scene " + str(sceneIndex + 1) + ", who says:")
    print('"' + play[actIndex][sceneIndex][characterName][lineIndex] + '"')

    #Now we have to build the list of choices the user
    #will choose from
    choices = [characterName]

    #Get the list of characters in the scene
    characterList = list(play[actIndex][sceneIndex].keys())
    characterList.remove(characterName)
    if len(characterList) > 3:
        #Pick 3 random alternate choices from the scene
        for i in range(3):
            idx = random.randint(0, len(characterList) - 1)
            choices.append(characterList[idx])
            characterList.pop(idx)
    else:
        #There are 4 or fewer characters in the scene
        #Just add all the characters to the list
        choices += characterList
            
    #Place the correct character in a random position
    #in the list of answers
    correctPos = random.randint(0, len(choices) - 1)
    tmp = choices[correctPos]
    choices[correctPos] = choices[0]
    choices[0] = tmp
        
    #Print the choices
    answerList = 'abcd'
    for i in range(len(choices)):
        print(answerList[i] + ") " + choices[i])
    
    return answerList[correctPos]


def main():
   # opens the file and reads it.
    inFilename = sys.argv[1]
    fin = open(inFilename, 'r')

    #gets the title
    title = fin.readline()
    title = title.strip('\n')

    play = readPlay(inFilename)
  
    # prints a greeting message + the title of the play
    print('Hello and Welcome to the quiz for' + title)
    
    numQuestions = 0
    numCorrect = 0
    yesToPlay = True
    while yesToPlay == True:
        #makes random act and scene indexes
        actIdx = random.randint(0, len(play)-1)
        sceneIdx = random.randint(0, len(play[actIdx])-1)
  
        #makes random character
        characters = list(play[actIdx][sceneIdx].keys())
        characterName = characters[random.randint(0, len(characters)-1)]
        #random line choice
        line = play[actIdx][sceneIdx][characterName]
        lineIdx = random.randint(0, len(line)-1)
        #increases the number pf questions that have been asled
        numQuestions += 1
        #assigns the right answer to var.
        corrAns = printQuestion(play,actIdx, sceneIdx, characterName, lineIdx, numQuestions)
        #asks for input
        answer = input('Choose a,b,c,d  :  ')
        while answer not in 'abcd':
            answer = input('What is the correct answer?  :  ')
            
            if answer not in 'abcd':
                print('Input is not valid. Please input either "a", "b", "c", or "d"')
    #compares user answer to real answer
        if answer == corrAns:
            decided = False
            numCorrect += 1
            print('Perfect !!! Current Score: ' + str(numCorrect) + '/' + str(numQuestions))
            #sees if the user wants to continue
            while decided == False:
                cont = input('Want to continue? (y/n)')
                if cont == 'y':
                    decided = True
                elif cont == 'n':
                    decided = True
                    yesToPlay = False
                  
            #same thing but if the answer is not equal to the real snwer
        elif corrAns != answer:
            decided = False
            print('This is wrong. The correct answer is: ' + corrAns)
            print('Current Score: ' + str(numCorrect) + '/' + str(numQuestions))
            
            while decided == False:
                cont = input('Want to continue? (y/n)')
                if cont == 'y':
                    decided = True
                elif cont == 'n':
                    decided = True
                    yesToPlay = False
   # prints the results of the quiz
    print('Final Score: ' + str(numCorrect) + '/' + str(numQuestions))

    
    fin.close()
main()
    
