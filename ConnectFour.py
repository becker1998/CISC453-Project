import numpy as np
import random as rand
from Agent import *
from Board import Board
from QAgent import QAgent

class ConnectFour:
    def __init__(self, alpha, gamma):
        self.turn = rand.randint(1,2)
        self.rows = 6
        self.cols = 7
        self.alpha = 0.01
        self.gamma = 0.01
        self.actions = np.zeros(self.cols, dtype = int)
        self.twoconnections = []
        self.threeconnections = []
        self.board = Board(self.rows, self.cols)
        self.p1 = QAgent(1, self.actions, self.alpha, self.gamma, 2)
        self.p2 = QAgent(2, self.actions, self.alpha, self.gamma, 1)
        
    def checkForWin(self, board, lastPiece):
        topscore = 0
        botscore = 0
        toprightscore = 0
        botleftscore = 0
        rightscore = 0
        leftscore = 0
        botrightscore = 0
        topleftscore = 0
        # check which player put in the last piece
        player = board[lastPiece[0], lastPiece[1]]
        
        # check top and bot scores
        i = lastPiece[0]
        j = lastPiece[1]
        while i - 1 >= 0 and board[i - 1][j] == player:
            topscore += 1
            i -= 1
        i = lastPiece[0]
        j = lastPiece[1]
        while i + 1 <= 5 and board[i + 1][j] == player:
            botscore += 1
            i += 1
        if topscore + botscore >= 3:
            return player

        # check topright and botleft scores
        i = lastPiece[0]
        j = lastPiece[1]
        while i - 1 >= 0 and j + 1 <= 6 and board[i - 1][j + 1] == player:
            toprightscore += 1
            i -= 1
            j += 1
        i = lastPiece[0]
        j = lastPiece[1]
        while i + 1 <= 5 and j - 1 >= 0 and board[i + 1][j - 1] == player:
            botleftscore += 1
            i += 1
            j -= 1
        if toprightscore + botleftscore >= 3:
            return player

        # check right and left scores
        i = lastPiece[0]
        j = lastPiece[1]
        while j + 1 <= 6 and board[i][j + 1] == player:
            rightscore += 1
            j += 1
        i = lastPiece[0]
        j = lastPiece[1]
        while j - 1 >= 0 and board[i][j - 1] == player:
            leftscore += 1
            j -= 1
        if rightscore + leftscore >= 3:
            return player

        # check botright and topleft scores
        i = lastPiece[0]
        j = lastPiece[1]
        while i + 1 <= 5 and j + 1 <= 6 and board[i + 1][j + 1] == player:
            botrightscore += 1
            i += 1
            j += 1
        i = lastPiece[0]
        j = lastPiece[1]
        while i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == player:
            topleftscore += 1
            i -= 1
            j -= 1
        if botrightscore + topleftscore >= 3:
            return player
        
        # we didn't win
        return 0

    def checkBoardState(self, player, rows, cols, board):
        # array of all the connections of three for the given player
        twoconnections = []
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
                    if topscore + botscore == 2 or topscore + botscore == 3:
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
                        if topscore + botscore == 2 and tempconnection not in twoconnections:
                            twoconnections.append(tempconnection)
                        if topscore + botscore == 2 and tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    # check if bot slot is free
                    if tempconnection[2][0] + 1 <= 5 and board[tempconnection[2][0] + 1, tempconnection[2][1]] == 0:
                        tempconnection.append([tempconnection[2][0] + 1, tempconnection[2][1]])
                        tempconnection.sort()
                        if topscore + botscore == 2 and tempconnection not in twoconnections:
                            twoconnections.append(tempconnection)
                        if topscore + botscore == 2 and tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    
                    # check topright and botleft scores
                    while i - 1 >= 0 and j + 1 <= 6 and board[i - 1, j + 1] == player:
                        toprightscore += 1
                    while i + 1 <= 5 and j - 1 >= 0 and board[i + 1, j - 1] == player:
                        botleftscore += 1
                    if toprightscore + botleftscore == 2 or toprightscore + botleftscore == 3:
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
                        if topscore + botscore == 2 and tempconnection not in twoconnections:
                            twoconnections.append(tempconnection)
                        if topscore + botscore == 2 and tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    # check if botleft slot is free
                    if tempconnection[2][0] + 1 <= 5 and tempconnection[2][1] - 1 >= 0 and board[tempconnection[2][0] + 1, tempconnection[2][1] - 1] == 0:
                        tempconnection.append([tempconnection[2][0] + 1, tempconnection[2][1] - 1])
                        tempconnection.sort()
                        if topscore + botscore == 2 and tempconnection not in twoconnections:
                            twoconnections.append(tempconnection)
                        if topscore + botscore == 2 and tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)

                    # check right and left scores
                    while j + 1 <= 6 and board[i, j + 1] == player:
                        rightscore += 1
                    while j - 1 >= 0 and board[i, j - 1] == player:
                        leftscore += 1
                    if rightscore + leftscore == 2 or rightscore + leftsocre == 3:
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
                        if topscore + botscore == 2 and tempconnection not in twoconnections:
                            twoconnections.append(tempconnection)
                        if topscore + botscore == 2 and tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    # check if left slot is free 
                    if tempconnection[0][1] - 1 >= 0 and board[tempconnection[0][0], tempconnection[0][1] - 1] == 0:
                        tempconnection.append([tempconnection[0][0], tempconnection[0][1] - 1])
                        tempconnection.sort()
                        if topscore + botscore == 2 and tempconnection not in twoconnections:
                            twoconnections.append(tempconnection)
                        if topscore + botscore == 2 and tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)

                    # check botright and topleft scores
                    while i + 1 <= 5 and j + 1 <= 6 and board[i - 1, j] == player:
                        botrightscore += 1
                    while i - 1 >= 0 and j - 1 >= 0 and board[i + 1, j] == player:
                        topleftscore += 1
                    if botrightscore + topleftscore == 2 or botrightscore + topleftscore == 3:
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
                        if topscore + botscore == 2 and tempconnection not in twoconnections:
                            twoconnections.append(tempconnection)
                        if topscore + botscore == 2 and tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
                    # check if topleft slot is free
                    if tempconnection[0][0] - 1 >= 0 and tempconnection[0][1] - 1 >= 0 and board[tempconnection[0][0] - 1, tempconnection[0][1] - 1] == 0:
                        tempconnection.append([tempconnection[0][0] - 1, tempconnection[0][1] - 1])
                        tempconnection.sort()
                        if topscore + botscore == 2 and tempconnection not in twoconnections:
                            twoconnections.append(tempconnection)
                        if topscore + botscore == 2 and tempconnection not in threeconnections:
                            threeconnections.append(tempconnection)
        self.twoconnections = twoconnections
        self.threeconnections = threeconnections
        
    def printGame (self,board):
        '''prints the game to the monitor'''

        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in board]))

    def returnP1QTable(self):
        return self.p1.getQTable()
    def returnP1Tag(self):
        return self.p1.getPTag()
    def returnP2QTable(self):
        return self.p2.getQTable()
    def returnP2Tag(self):
        return self.p2.getPTag()
        
    def play (self):
        '''runs the game with 2 q agents'''

        

        checkWin = 0
        while (checkWin == 0 and not self.board.isBoardFilled()):
            insertP1 = self.p1.choice(self.board.getBoard(), self.board.isBoardEmpty())
            self.board.insertPiece(1, insertP1)
            
            #print("p1's move:")
            #print(self.board.getBoard())
            lastPiece = self.board.getLastPiece()
            checkWin = self.checkForWin(self.board.getBoard(), lastPiece)
            if (checkWin != 0 or self.board.isBoardFilled()):
                break
            insertP2 = self.p2.choice(self.board.getBoard(), self.board.isBoardEmpty())
            self.board.insertPiece(2, insertP2)
            #print("p2's move:")
            #print(self.board.getBoard())
            
            lastPiece = self.board.getLastPiece()
            #print ("last piece =", lastPiece)
            #needs while loop to complete game
            checkWin = self.checkForWin(self.board.getBoard(), lastPiece)
        if checkWin == 0:
            print ("no one won")
        elif checkWin == 1:
            print ("p1 won")
        elif checkWin == 2:
            print ("p2 won")

            
def qValues():
    snIn = open("Q_Results.txt", "w")
    snIn.write("Q Averages for alpha and gamma starting at 0.01 and ending at 1 with intervals of 0.05\n")
    

    for i in range (1,100,50):
        alpha = i / 100
        for j in range(1, 100, 50):
            gamma = j / 100
            snIn.write("\n")
            snIn.write("alpha: " + str(alpha) + " gamma: " + str(gamma))
            game = ConnectFour(alpha, gamma)
            game.play()
            average1 = sum(game.returnP1QTable()) / len(game.returnP1QTable())
            average2 = sum(game.returnP2QTable()) / len(game.returnP2QTable())
            snIn.write("\n") 
            snIn.write("Player 1 Q Average: " + str(round(average1, 3)))
            snIn.write("\n")  
            snIn.write("Player 2 Q Average: " + str(round(average2, 3)))
            snIn.write("\n")          
    
    
    
    snIn.close()

qValues()
