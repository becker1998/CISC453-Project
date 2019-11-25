import random
import numpy as np

class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.lastPiece = []
        self.board = np.zeros(shape=(rows, cols), dtype=int)

    def isSlotFilled(self, row, col):
        print("slot row: ", row)
        print("slot col: ", col)
        return self.board[row][col] != 0

    def isColFilled(self, col):
        print("board:")
        print(self.board)
        return self.board[0][col] != 0

    def insertPiece(self, player, col):
        if not self.isColFilled(col):
            for i in range(self.rows - 1, -1, -1):
                print("hi")
                if not self.isSlotFilled(i, col):
                    self.board[i][col] = player
                    print("Board 3")
                    print(self.board)
                    self.lastPiece = [i, col]
                    return True
        return False

    def getBoard(self):
        return self.board

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols
    def getLastPiece (self):
        '''get ethod for which player inserted a coin last'''
        return self.lastPiece;
    def isBoardFilled(self):
        for j in range(self.cols):
            if self.board[j][0] == 0:
                return False
        return True
    
    def isBoardEmpty(self):
        initBoard = np.zeros(shape=(6,7), dtype=int)
        return np.array_equal(initBoard, self.board)
    
    def getActions(self):
        actions = []
        for i in range(self.cols):
            if self.isColFilled == False:
                actions.append(i)
        return actions

x=Board(6,7)
print(x.board)
