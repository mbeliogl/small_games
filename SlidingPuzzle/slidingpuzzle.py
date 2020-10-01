
import random 

class SlidingPuzzle:
    def __init__(self, numRows, numColumns):
        boardList = []
        a = 0
        for i in range(numRows):
            insideList = []
            for j in range(numColumns):
               insideList.append(a)
               a += 1
            boardList.append(insideList)
        
        self.board = boardList
        self.solved = False
        self.numRows = numRows
        self.numColumns = numColumns

    # returning the board in its initial state 
    def getStartingBoard(self):
        boardList = []
        a = 0
        for i in range(self.numRows):
            insideList = []
            for j in range(self.numColumns):
               insideList.append(a)
               a += 1
            boardList.append(insideList)
        return boardList

    # formatting the puzzle and printing to command line 
    def displayPuzzle(self):
        i = 0
        for row in self.board:
            line = ''
            for number in self.board[i]:
                line += str(number)
                #alligns the puzzle nicely 
                if len(str(number)) == 1:
                    line += '  '
                else:
                    line += ' '
            #board is printed
            print(str(line))          
            i += 1
                
    # defining the move functionality   
    def move(self, rowIdx, colIdx):
        rowOfZero = 0 
        colOfZero = 0
        for i in self.board:
            if 0 in i:
                #gets the row index and the column index of the 0
                rowOfZero = self.board.index(i)
                colOfZero = i.index(0)
                zeropos = self.board.index(i), i.index(0)
       
        other_num = self.board[rowIdx][colIdx]   #number to switch zero with 
        
        #switches 0 and the number from legal moves on board 
        self.board[rowIdx][colIdx] = 0 
        self.board[rowOfZero][colOfZero] = other_num

    # defining the returning a list of all legal moves on the current board
    def legalMoves(self):
        rowOfZero = 0
        colOfZero = 0
        for i in self.board:
            if 0 in i:
                rowOfZero = self.board.index(i)
                colOfZero = i.index(0)
                zeropos = self.board.index(i), i.index(0)
        
        legalMoves = []
        # checks if there are spaces near 0 and saves them in form of a tupple with coordinates or row and column
        if rowOfZero - 1 >= 0:
            move1 = rowOfZero - 1, colOfZero
            legalMoves.append(move1)
        if rowOfZero + 1 <= len(self.board)-1:
            move2 = rowOfZero + 1, colOfZero
            legalMoves.append(move2)
        if colOfZero - 1 >= 0:
            move3 = rowOfZero, colOfZero - 1
            legalMoves.append(move3)
        if colOfZero + 1 <= len(self.board[rowOfZero]) - 1:
            move4 = rowOfZero, colOfZero +1
            legalMoves.append(move4)
            
        return legalMoves
        
    # choosing a random move from legalMoves() to scramble n amount of times (depending on difficulty)
    def scramble(self, numMoves):

        for i in range(numMoves):
            legal_moves = self.legalMoves()
            num_legal_moves = len(legal_moves)
            random_idx = random.randint(0, num_legal_moves-1) #index of random move

            move = legal_moves[random_idx]
            row = move[0]
            col = move[1]

            self.move(row,col)        

    # this method checks if the puzzle is solved 
    def isSolved(self):

        board_list = self.getStartingBoard() #initial board config 
        if self.board == board_list:
            self.solved = True

        return self.solved

