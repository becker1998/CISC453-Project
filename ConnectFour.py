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
        while lastPiece[0] - 1 >= 0 and board[lastPiece[0] - 1][lastPiece[1]] == player:
            topscore += 1
        while lastPiece[0] + 1 <= 5 and board[lastPiece[0] - 1][ lastPiece[1]] == player:
            botscore += 1
        if topscore + botscore >= 4:
            return player

        # check topright and botleft scores
        print ("check board: ", board)
        print ("check lastPiece: ", lastPiece)
        while lastPiece[0] - 1 >= 0 and lastPiece[1] + 1 <= 6 and board[lastPiece[0] - 1, lastPiece[1] + 1] == player:
            toprightscore += 1
        while lastPiece[0] + 1 <= 5 and lastPiece[1] - 1 >= 0 and board[lastPiece[0] + 1, lastPiece[1] - 1] == player:
            botleftscore += 1
        if toprightscore + botleftscore >= 4:
            return player

        # check right and left scores
        while lastPiece[1] + 1 <= 6 and board[lastPiece[0], lastPiece[1] + 1] == player:
            rightscore += 1
        while lastPiece[1] - 1 >= 0 and board[lastPiece[0], lastPiece[1] - 1] == player:
            leftscore += 1
        if rightscore + leftscore >= 4:
            return player

        # check botright and topleft scores
        while lastPiece[0] + 1 <= 5 and lastPiece[1] + 1 <= 6 and board[lastPiece[0] + 1, lastPiece[1] + 1] == player:
            botrightscore += 1
        while lastPiece[0] - 1 >= 0 and lastPiece[1] - 1 >= 0 and board[lastPiece[0] - 1, lastPiece[1] - 1] == player:
            topleftscore += 1
        if botrightscore + topleftscore >= 4:
            return player
        
        # we didn't win
        return 0

    def checkBoardState(self, player, rows, cols, board):
        # array of all the connections of three for the given player
        threeconnections = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != 0:
                    tempconnection = []
                    topscore = 1
                    botscore = 1
                    toprightscore = 1
                    botleftscore = 1
                    rightscore = 1
                    leftscore = 1
                    botrightscore = 1
                    topleftscore = 1
                    
                    # check top and bot scores
                    while i - 1 >= 0 and board[i - 1, j] == player:
                        topscore += 1
                    while i + 1 <= 5 and board[i + 1, j] == player:
                        botscore += 1
                    if topscore + botscore == 3:
                        tempconnection.append([i, j])
                        for k in range(1, topscore):
                            tempconnection.append([i - k, j])
                        for k in range(1, botscore):
                            tempconnection.append([i + k, j])
                    tempconnection.sort()
                    # check if top slot is free
                    if tempconnection[0][0] - 1 >= 0 and board[tempconnection[0][0] - 1, tempconnection[0][1]] == 0:
                        tempconnection.append([tempconnection[0][0] - 1, tempconnection[0][1]])
                        tempconnection.sort()
                        if tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    # check if bot slot is free
                    if tempconnection[2][0] + 1 <= 5 and board[tempconnection[2][0] + 1, tempconnection[2][1]] == 0:
                        tempconnection.append([tempconnection[2][0] + 1, tempconnection[2][1]])
                        tempconnection.sort()
                        if tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    
                    # check topright and botleft scores
                    while i - 1 >= 0 and j + 1 <= 6 and board[i - 1, j + 1] == player:
                        toprightscore += 1
                    while i + 1 <= 5 and j - 1 >= 0 and board[i + 1, j - 1] == player:
                        botleftscore += 1
                    if toprightscore + botleftscore == 3:
                        tempconnection.append([i, j])
                        for k in range(1, toprightscore):
                            tempconnection.append([i - k, j + k])
                        for k in range(1, botleftscore):
                            tempconnection.append([i + k, j - k])
                    tempconnection.sort()
                    # check if topright slot is free
                    if tempconnection[0][0] - 1 >= 0 and tempconnection[0][1] + 1 <= 6 and board[tempconnection[0][0] - 1, tempconnection[0][1] + 1] == 0:
                        tempconnection.append([tempconnection[0][0] - 1, tempconnection[0][1] + 1])
                        tempconnection.sort()
                        if tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    # check if botleft slot is free
                    if tempconnection[2][0] + 1 <= 5 and tempconnection[2][1] - 1 >= 0 and board[tempconnection[2][0] + 1, tempconnection[2][1] - 1] == 0:
                        tempconnection.append([tempconnection[2][0] + 1, tempconnection[2][1] - 1])
                        tempconnection.sort()
                        if tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)

                    # check right and left scores
                    while j + 1 <= 6 and board[i, j + 1] == player:
                        rightscore += 1
                    while j - 1 >= 0 and board[i, j - 1] == player:
                        leftscore += 1
                    if rightscore + leftscore == 3:
                        tempconnection.append([i, j])
                        for k in range(1, rightscore):
                            tempconnection.append([i, j + k])
                        for k in range(1, leftscore):
                            tempconnection.append([i, j - k])
                    tempconnection.sort()
                    # check if right slot is free
                    if tempconnection[2][1] + 1 <= 6 and board[tempconnection[2][0], tempconnection[2][1] + 1] == 0:
                        tempconnection.append([tempconnection[2][0], tempconnection[2][1] + 1])
                        tempconnection.sort()
                        if tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    # check if left slot is free 
                    if tempconnection[0][1] - 1 >= 0 and board[tempconnection[0][0], tempconnection[0][1] - 1] == 0:
                        tempconnection.append([tempconnection[0][0], tempconnection[0][1] - 1])
                        tempconnection.sort()
                        if tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)

                    # check botright and topleft scores
                    while i + 1 <= 5 and j + 1 <= 6 and board[i - 1, j] == player:
                        botrightscore += 1
                    while i - 1 >= 0 and j - 1 >= 0 and board[i + 1, j] == player:
                        topleftscore += 1
                    if botrightscore + topleftscore == 3:
                        tempconnection.append([i, j])
                        for k in range(1, botrightscore):
                            tempconnection.append([i - k, j + k])
                        for k in range(1, topleftscore):
                            tempconnection.append([i + k, j - k])
                    tempconnection.sort()
                    # check if botright slot is free
                    if tempconnection[2][0] + 1 <= 5 and tempconnection[2][1] + 1 <= 6 and board[tempconnection[2][0] + 1, tempconnection[2][1] + 1] == 0:
                        tempconnection.append([tempconnection[2][0] + 1, tempconnection[2][1] + 1])
                        tempconnection.sort()
                        if tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    # check if topleft slot is free
                    if tempconnection[0][0] - 1 >= 0 and tempconnection[0][1] - 1 >= 0 and board[tempconnection[0][0] - 1, tempconnection[0][1] - 1] == 0:
                        tempconnection.append([tempconnection[0][0] - 1, tempconnection[0][1] - 1])
                        tempconnection.sort()
                        if tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
        return threeconnections
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
        print("insert : ", insertP1)
        board.insertPiece(1,insertP1-1)
        insertP2 = p2.choice(board.getBoard(), board.isBoardEmpty())
        board.insertPiece(2,insertP2-1)
        
        lastPiece = board.getLastPiece()
        
        b = board.getBoard().T
        print("Board 2: ", board.getBoard())
        self.printGame(b)
        b = board.getBoard().T
        #needs while loop to complete game
        checkWin = self.checkForWin(board.getBoard(), lastPiece)
        #while checkWin == 0:
            

game = ConnectFour(6,7,1,1)
game.play()
