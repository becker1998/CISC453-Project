import random
import numpy as np

class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.lastPiece = []
        self.board = [[0] * rows] * cols

    def isSlotFilled(self,col, row):
        print("slot row: ", row)
        print("slot col: ", col)
        return self.board[col][row] != 0

    def isColFilled(self, col):
        print("is col: ", col)
        print("board: ", self.board)
        return self.board[col][0] != 0

    def insertPiece(self, player, col):
        if not self.isColFilled(col):
            for i in range(self.rows - 1, -1, -1):
                print(i)
                if not self.isSlotFilled(col, i):
                    self.board[col][i] = player
                    self.lastPiece = [col, i]
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
        initBoard = [[0] * self.rows] * self.cols
        if initBoard == self.board:
            return True
        return False
    
    def getActions(self):
        actions = []
        for i in range(self.cols):
            if self.isColFilled == False:
                actions.append(i)
        return actions
