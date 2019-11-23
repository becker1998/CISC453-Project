import random
import numpy as np

class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.lastPiece = []
        self.board = [[0] * cols] * rows

    def isSlotFilled(self, row, col):
        return self.board[row][col] != 0

    def isColFilled(self, col):
        return self.board[0][col] != 0

    def insertPiece(self, player, col):
        if not isColFilled(col):
            for i in range(self.cols - 1, -1, -1):
                if not isSlotFilled(i, col):
                    self.board[i][col] = player
                    self.lastPiece = [i, col]
                    return True
        return False

    def checkForWin(self):
        topscore = 1
        botscore = 1
        toprightscore = 1
        botleftscore = 1
        rightscore = 1
        leftscore = 1
        botrightscore = 1
        topleftscore = 1
        # check which player put in the last piece
        player = self.board[self.lastPiece[0], self.lastPiece[1]]

        # check top and bot scores
        while self.lastPiece[0] - 1 >= 0 and self.board[self.lastPiece[0] - 1, self.lastPiece[1]] == player:
            topscore += 1
        while self.lastPiece[0] + 1 <= 5 and self.board[self.lastPiece[0] + 1, self.lastPiece[1]] == player:
            botscore += 1
        if topscore + botscore >= 4:
            return player

        # check topright and botleft scores
        while self.lastPiece[0] - 1 >= 0 and self.lastPiece[1] + 1 <= 6 and self.board[self.lastPiece[0] - 1, self.lastPiece[1] + 1] == player:
            toprightscore += 1
        while self.lastPiece[0] + 1 <= 5 and self.lastPiece[1] - 1 >= 0 and self.board[self.lastPiece[0] + 1, self.lastPiece[1] - 1] == player:
            botleftscore += 1
        if toprightscore + botleftscore >= 4:
            return player

        # check right and left scores
        while self.lastPiece[1] + 1 <= 6 and self.board[self.lastPiece[0], self.lastPiece[1] + 1] == player:
            rightscore += 1
        while self.lastPiece[1] - 1 >= 0 and self.board[self.lastPiece[0], self.lastPiece[1] - 1] == player:
            leftscore += 1
        if rightscore + leftscore >= 4:
            return player

        # check botright and topleft scores
        while self.lastPiece[0] + 1 <= 5 and self.lastPiece[1] + 1 <= 6 and self.board[self.lastPiece[0] + 1, self.lastPiece[1] + 1] == player:
            botrightscore += 1
        while self.lastPiece[0] - 1 >= 0 and self.lastPiece[1] - 1 >= 0 and self.board[self.lastPiece[0] - 1, self.lastPiece[1] - 1] == player:
            topleftscore += 1
        if botrightscore + topleftscore >= 4:
            return player
        
        # we didn't win
        return 0
        
    def isBoardFilled(self):
        for j in range(self.cols):
            if self.board[0][j] == 0:
                return False
        return True
    def getActions(self):
        actions = []
        for i in range(self.cols):
            if isColFilled == False:
                actions.append(i)
        return actions

x = Board(6, 7)
print (x.board)
