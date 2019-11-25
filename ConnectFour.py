import numpy as np
import random as rand
from Agent import *
from Board import Board
from QAgent import QAgent

class ConnectFour:
    def __init__(self, rows, cols, alpha, gamma):
        self.turn = rand.randint(1,2)
        self.rows = rows
        self.cols = cols
        self.alpha = alpha
        self.gamma = gamma
        self.actions = np.zeros(cols, dtype = int)
    def checkForWin(self, board, lastPiece):
        topscore = 1
        botscore = 1
        toprightscore = 1
        botleftscore = 1
        rightscore = 1
        leftscore = 1
        botrightscore = 1
        topleftscore = 1
        # check which player put in the last piece
        player = board[lastPiece[0], lastPiece[1]]
        
        # check top and bot scores
        while lastPiece[0] - 1 >= 0 and board[lastPiece[0] - 1][lastPiece[1] + 1] == player:
            topscore += 1
        while lastPiece[0] + 1 <= 5 and board[lastPiece[0] - 1][ lastPiece[1] + 1] == player:
            botscore += 1
        if topscore + botscore >= 4:
            return player

        # check topright and botleft scores
        print ("check board: ", board)
        print ("check lastPiece: ", lastPiece)
        while lastPiece[0] - 1 >= 0 and lastPiece[1] + 1 <= 6 and board[lastPiece[0] - 1][ lastPiece[1] + 1] == player:
            toprightscore += 1
        while lastPiece[0] + 1 <= 5 and lastPiece[1] - 1 >= 0 and board[lastPiece[0] + 1][ lastPiece[1] - 1] == player:
            botleftscore += 1
        if toprightscore + botleftscore >= 4:
            return player

        # check right and left scores
        while lastPiece[1] + 1 <= 6 and board[lastPiece[0]][ lastPiece[1] + 1] == player:
            rightscore += 1
        while lastPiece[1] - 1 >= 0 and board[lastPiece[0]][lastPiece[1] - 1] == player:
            leftscore += 1
        if rightscore + leftscore >= 4:
            return player

        # check botright and topleft scores
        while lastPiece[0] + 1 <= 5 and lastPiece[1] + 1 <= 6 and board[lastPiece[0] + 1][ lastPiece[1] + 1] == player:
            botrightscore += 1
        while lastPiece[0] - 1 >= 0 and lastPiece[1] - 1 >= 0 and board[lastPiece[0] - 1][lastPiece[1] - 1] == player:
            topleftscore += 1
        if botrightscore + topleftscore >= 4:
            return player
        
        # we didn't win
        return 0

    def printGame (self,board):
        '''prints the game to the monitor'''

        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in board]))
        
    def play (self):
        '''runs the game with 2 q agents'''

        
        board = Board(self.rows, self.cols)
        p1 = QAgent(1, self.actions, self.alpha, self.gamma, 2)
        p2 = QAgent(2, self.actions, self.alpha, self.gamma, 1)
        
        insertP1 = p1.choice(board.getBoard(), board.isBoardEmpty())
        print("insert : ", insertP1-1)
        board.insertPiece(1,insertP1-1)
        insertP2 = p2.choice(board.getBoard(), board.isBoardEmpty())
        board.insertPiece(2,insertP2-1)
        
        lastPiece = board.getLastPiece()
        lastPiece[0] -= 1
        lastPiece[1] -= 1
        b = board.getBoard().T
        print("Board 2: ", board.getBoard())
        self.printGame(b)
        b = board.getBoard().T
        #needs while loop to complete game
        print(lastPiece)
        checkWin = self.checkForWin(board.getBoard(), lastPiece)
        #while checkWin == 0:
    

game = ConnectFour(6,7,1,1)
game.play()
