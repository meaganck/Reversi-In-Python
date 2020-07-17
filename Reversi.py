from __future__ import print_function # allows Python to use print as a function

# Part 1: Create nxn board and output it

def printBoard(board, n):
        """Outputs board"""
        
                  
        letter = ['*','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        print(' ', end=' ')

        # prints letters in first row
        for i in range(ROW-1):
                print (letter[i+1], end ="  ")
        print( "\n")

        # prints colums
        for row in range(n):
                print (letter[row+1], end = " ") # prints letter at the begining of row

                for col in range(n):
                    print(board[row+1][col+1], end = " ")

                print("\n")


def findOpponent(playerColour):
        """Finds and returns colour of opponent"""

        if playerColour == "W":
               opponent = "B"
        elif playerColour == "B":
                opponent = "W"
        else:
                print ("Invalid colour")
                opponent = "Z"
        return opponent


def positionInBounds(n, row, col):
        """Retruns true if position is on board, and false if outside"""
        if (1 <= row and row  <= n) and (1 <= col and col <= n):
                return True
        else:
                return False


def legalDirection(board, n, row, col, colour, deltaRow, deltaCol):
        """Returns true if there's a legal move, else returns false"""

         # checks if deltaRow == deltaCol == 0, which is an invalid direction
        if (deltaRow == 0) and (deltaCol == 0):
                print("Failed deltaRow and col == 0")
                return False

        opponent = findOpponent(colour)
        currentRow = row + deltaRow
        currentCol = col + deltaCol

    # move must have a valid positon on the board and opponent has to be adjacent
        if (not positionInBounds(n, currentRow, currentCol)) or board[currentRow][currentCol] != opponent:
                print("Failed 2nd condition")
                return False
        else:
                currentRow += deltaRow
                currentCol += deltaCol

            # searches through a direction
        while positionInBounds(n, currentRow, currentCol):
                tile = board[currentRow][currentCol]

                # if it hits its own colour, then found a valid move
                if tile == colour:
                        print("Passed: legal move")
                        return True

                #no move if there's an empty spot
                elif tile == 'U':
                        print("Failed 3rd condition")
                        return False

                # keeps on checkint if opponent is the tile
                else:
                        currentRow += deltaRow
                        currentCol += deltaCol


        print("Failed default")
        return False # found no move


def playMove(board, n, playedRow, playedCol, colour):
        """Plays the desired move"""

        row = playedRow
        col = playedCol
        numFlips = 0
        opponent = findOpponent(colour)
        board[row][col] = colour

            # not sure if this works!!!!!!!!!!!!
            # for ref: xrange(start, stop, step)
        for deltaRow in range(-1, 2):
                for deltaCol in range(-1, 2):
                        row = playedRow + deltaRow
                        col = playedCol + deltaCol
                        checking = True

                        while checking:
                                tile = board[row][col]

                                if tile == opponent:
                                      row +=deltaRow
                                      col += deltaCol

                                elif tile == colour:
                                      flipping = True
                                      checking = False
                                else:
                                    flipping = False
                                    checking = False
                                    continue

                        row = playedRow + deltaRow
                        col = playedCol + deltaCol

                        while flipping:
                                tile = board[row][col]

                                #if tile is opponent, then flip colour
                                if tile == opponent:
                                        board[row][col] = colour
                                        row += deltaRow
                                        col += deltaCol
                                        numFlips +=1
                                else:
                                        flipping = False
        return numFlips


def userTurn(board, n, userColour, userRow, userCol):
        """Validates user's move"""
        for deltaRow in range(-1, 2):
                 for deltaCol in range(-1, 2):
                         if legalDirection(board, n, userRow, userCol, userColour, deltaRow, deltaCol):
                                 return True # move is valid
        return False # did'f find a valid move


def checkBoard(board, n, colour):
        """Returns 1 if there is a legal move, and 0 if no moves"""
        for row in range(1, n+1):
                for col in range(1, n+1):
                        piece = board[row][col]

                        # checks for empty space
                        if piece == 'U':
                                for deltaRow in range(-1, 2):
                                        for deltaCol in range(-1,2):
                                                # if there is a legal move, calculates the score
                                                if legalDirection(board, n, row,col, colour, deltaRow, deltaCol):
                                                        return 1
        return 0 # did not find a legal move

def colourGoneOrBoardFull(board, n):
        """checks if a colour is off the board, and if board is full"""
        whiteOnBoard = False
        blackOnBoard = False
        boardFull = True

        for row in range(1, n+1):
                for col in range(1, n+1):
                        # if white is on board
                        if board[row][col] == 'W':
                                whiteOnBoard = True
                        # if black is on baord
                        elif board[row][col] == 'B':
                                blackOnBoard = True
                        # if there is an empty space left
                        elif board[row][col] == 'U':
                                boardFull = False

        # if any of these conditions are true, returns true
        if (not blackOnBoard) or (not whiteOnBoard) or (boardFull):
                return True
        else:
                return False


def calcWinner(board, n):
        """Finds winner, player with most colours"""
        numWhite = 0
        numBlack = 0

        for row in range(1, n+1):
                for col in range(1, n+1):
                        # point for white
                        if board[row][col] == 'W':
                                numWhite += 1
                        # point for black
                        elif board[row][col] == 'B':
                                numBlack += 1
        # white wins
        if numWhite > numBlack:
                return 'W'
        # black wins
        elif numWhite < numBlack:
                return 'B'
        # it's a tie
        else:
                return 'T'

def calcScore(board, n, playedRow, playedCol, colour):
        """Finds score of move"""
        score = 0
        total = 0
        opponent = findOpponent(colour)

        for deltaRow in range(-1, 2):
                for deltaCol in range(-1,2):
                        row = playedRow + deltaRow
                        col = playedCol + deltaCol
                        score = 0
                        checking = True

                        while checking:
                                tile = board[row][col]

                                # if its opponent
                                if tile == opponent:
                                        row += deltaRow
                                        col += deltaCol
                                        score += 1
                                # if its own colour
                                elif tile == colour:
                                        flipping = True
                                        checking = False
                                # unoccupied spot, cannot flip
                                else:
                                        flipping = False
                                        checking = False
                                        continue
                        row = playedRow + deltaRow
                        col = playedCol + deltaCol

                        # if it could flip add to score
                        if flipping:
                                total += score
        return total


def compTurn(board, n, colour):
        """returns row, col for comp to play"""
        highScore = 0
        newScore = 0

        # if there is no move, returns -1 for row and col
        bestRow = -1
        bestCol = -1

        for row in range(1, n+1):
                for col in range(1, n+1):
                        piece = board[row][col]

                        # checks for empty space
                        if piece == 'U':
                                for deltaRow in range(-1, 2):
                                        for deltaCol in range(-1, 2):
                                                # if there is a legal move, finds score
                                                print("TEST")
                                                if legalDirection(board, n, row, col, colour, deltaRow, deltaCol):
                                                        newScore = calcScore(board, n, row, col, colour)
                                                        print("newScore: ", newScore)

                                                        # compares current score with exisiting score
                                                        if newScore > highScore:
                                                                # if it is greater, changes the row and col
                                                                bestRow = row
                                                                bestCol = col
                                                                highScore = newScore
                coord = [bestRow , bestCol]
                return coord




# constants

MAX = 26
LETTERS = ['*','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# variables
playing = True
numTurns = 0
currentColour = 'W' # black plays first, when start of game changes colour
winnerFound = False
userPlay = True
compPlay = True

# gets dimension of board from user
n = input("Enter dimension of board: ")

# user selects what colour the computer plays
compColour = raw_input("Computer plays (B/W): ")

# determine colour of user using findOpponent
userColour = findOpponent(compColour) # make a check to see if user gave a valid colour

# Want below to be equivalent to board = [n+1][MAX]
ROW = n+1
COL = MAX

board = [['U'  for j in range (ROW)] for i in range(MAX)]


for row in range(ROW):
        for col in range(MAX):

                #postiton for White
                if  ((row == n/2 and col == n/2) or (row== n/2 +1 and col == n/2 + 1)):
                        board[row][col] = 'W'

                #position for Black
                elif ((row == n/2 and col == n/2 +1) or (row == n/2 + 1 and col == n/2)):
                        board[row][col] = 'B'


printBoard(board, n)

# starts game
while playing:
        numTurns +=1

         # add validation to check if end of game!!

        #determines whose turn it is
        if currentColour == 'W':
                currentColour = 'B'
        else: #in essense if the current colour is black
                currentColour = 'W'

        # computer's turn
        if compColour == currentColour:
                move = compTurn(board, n, compColour)
                print(move)

                # if there is a move
                if move[0] != -1:

                         # might work?
                        outputRow = letters[move[0]]
                        outputCol = letters[move[1]]
                        print("Computer places ", compColour, " at ", outputRow, outputCol)
                        playMove(board, n, move[0], move[1], compColour)
                        compPlay = True
                        printBoard(board, n)
                # no move
                else:
                        if userPlay:
                                print(compColour, "player has no valid move")
                        compPlay = False



    # user's turn
        else:
                # check if user can play, no move
                if checkBoard(board, n, userColour) == 0:
                        userPlay = False
                        if compPlay:
                                print(userColour, "player had no valid move")
                        # player can make a move
                else:
                        userPlay = True
                        userRow= raw_input("Enter a row: ")
                        userCol= raw_input("Enter a col for: ")

                        # convert to int
                        userRowNum = LETTERS.index(userRow)
                        userColNum = LETTERS.index(userCol)

                        print("You chose: row: ", userRowNum, "and col: ", userColNum)

                        # if valid move
                        if userTurn(board, n, userColour, userRowNum, userColNum):
                                playMove(board, n, userRowNum, userColNum, userColour)
                        # invalid move, comp wins
                        else:
                                print("Invalid move.")
                                playing = False
                                winnerFound = True
                                winner = compColour
                                continue
                        printBoard(board, n)




# end of game
if not winnerFound:
        pass

if winner == 'T':
        print("Draw!")
else:
        print("X player wins.")

