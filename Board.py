import random
import numpy as np

class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0] * cols] * rows 

    def isSlotFilled(self, row, col):
        return self.board[row][column] != 0

    def isColFilled(self, col):
        return self.board[0][col] != 0

    def insertPiece(self, player, col):
        if not isColFilled(col):
            for i in range(self.cols, -1, -1):
                if self.board[i][cols] == 0:
                    self.board[i][cols] = player
                    return True
                # check if we win here
        else:
            return False
            

    def isBoardFilled(self):
        for j in range(self.cols):
            if self.board[0][j] == 0:
                return False
        return True

x = Board(6, 7)
print (x.board)
