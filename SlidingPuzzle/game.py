
from slidingpuzzle import *

def main():
    
    print('----- The Puzzle Game! -----')
    print(f"\n--- Let's Talk Dimensions ---")
    height = int(input('How High? '))
    width = int(input('How Wide? '))
    print('\n')

    #creating board
    board = SlidingPuzzle(height, width)
    board.displayPuzzle()

    #getting difficulty level for Scramble()
    difficulty = input(f'\nChoose a Difficulty Level: [1, 2, 3]: ')
    difficulty = int(difficulty)

    # checks the answer and uses the scramble method to scramble the puzzle a given amount of times
    scrTimes = 0
    
    if difficulty == 1:
        scrTimes = 25
        
    if difficulty == 2:
        scrTimes = 50
        
    if difficulty == 3:
        scrTimes = 65

    board.scramble(scrTimes)
    print('\n----- Begin! -----\n')


    solved = False
    # continues the game while the puzzle is not solved yet #
    while solved == False:
        board.displayPuzzle()
        # askong user for row and column and using them to make a move
        #row = int(input('Choose a Row: '))
        #column = int(input('Choose a Column: '))
        
        legal_moves = board.legalMoves()
        num_moves = len(board.legalMoves())

        print(f"\nAllowed Moves: {legal_moves}")
        move_idx = int(input(f"\nPick a Move by Index. [0-{num_moves-1}]: "))
        print('\n')

        row = legal_moves[move_idx][0]
        col = legal_moves[move_idx][1]
        
        userMove = (row, col)
        
        # checks if the move is legal and if not requests a valid input
        if userMove not in board.legalMoves():
            print('-----Please Choose a Valid Move!-----')
            
        else:
            board.move(row, col)
            solved = board.isSolved()
            

    print('----- You Have Solved The Puzzle! -----')
    board.displayPuzzle()

main()
