import numpy as np
import random as rand
from Agent import *
import Board

class QAgent(Agent):
    def __init__(self, pTag, actions, alpha, gamma, oTag):
        super(Agent,self).__init__()
        self.qTable = [0] * 7
        self.alpha = alpha        
        self.gamma = gamma
        self.pTag = pTag #player tag
        self.oTag = oTag #opponent tag
        self.numCol = len(self.qTable)
        
    def chooseAction (self):
        '''chooses an actions'''
        actions = board.getActions()
        actionsTemp = []
        lenActions = len(actions)
        return rand.randint(0,lenActions - 1)
    def evalColFunction (self, col, board):
        '''heuristic functionthat will return a value from 1-4 based on
        the danger of losing/winning in the nexr state'''
        valCurrent = 0
        valOpp = 0
        column = []
        for i in range(6):
            column.append(board[i][col])
        #detrmines which plyers coin is sitting on top
        if (self.pTag in column):
            top = column.index(self.pTag)
        else:
            top = 6
        if (self.oTag in column):
            below = column.index(self.oTag)
        else:
            below = 6
        if top < below and top != 0:
            valCurrent +=1
            #loop down column while player has a connection
            for i in range (top+1, len(column)):
                if column[i] == self.pTag:
                    valCurrent += 1
                else:
                    break
        #opponents coin is on top
        elif below < top and below != 0:
            valOpp +=1
            for i in range (below+1, len(column)):
                if column[i] == self.oTag:
                    valOpp += 1
                else:
                    break
        return self.returnValue(valCurrent, valOpp)
    
    def evalRowFunction (self, col, numCol, board):
        '''heruistic function that counts number of roww connections'''
        valCurrent = 0
        valOpp = 0
        column = []
        for i in range(6):
            column.append(board[i][col])
        if (self.pTag in column):
            top = column.index(self.pTag)
        else:
            top = 6
        if (self.oTag in column):
            below = column.index(self.oTag)
        else:
            below = 6
        #since we are determining row connections
        #we dont care about the filled slots
        emptySpots = 5
        if top < below and top != 0:
            emptySpots = top - 1
        elif below < top and below != 0:
            emptySpots = below - 1
        #3 cases when we are on the first, last or middle columns
        if col == 0 and board[0][col] == 0:
            #if player coin is on same row
            j = 1
            while (j <= 6):
                if board[emptySpots][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                j += 1
            j = 1
            while (j <= 6):
                if board[emptySpots][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                j += 1
        #last column           
        elif col == 6 and board[0][col] == 0:
            #if player coin is on same row
            j = 5
            while (j >= 0):
                if board[emptySpots][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                j -= 1
            j = 5
            while (j >= 0):
                if board[emptySpots][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                j -= 1
        elif board[0][col] == 0:
            j = col + 1
            while (j <= 6):
                if board[emptySpots][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                j += 1
            j = col + 1
            while (j <= 6):
                if board[emptySpots][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                j += 1
            j = col - 1
            while (j >= 0):
                if board[emptySpots][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                j -= 1
            j = col - 1
            while (j >= 0):
                if board[emptySpots][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                j -= 1
        return self.returnValue(valCurrent, valOpp)
    
    def evalFirstDiagonalFunction (self, col, numCol, board):
        '''heuristic to evaluate diagonal connections'''
        valCurrent = 0
        valOpp = 0
        column = []
        for i in range(6):
            column.append(board[i][col])
        if (self.pTag in column):
            top = column.index(self.pTag)
        else:
            top = 6
        if (self.oTag in column):
            below = column.index(self.oTag)
        else:
            below = 6
        emptySpots = 5
        if top < below and top != 0:
            emptySpots = top - 1
        elif below < top and below != 0:
            emptySpots = below - 1
        if col == 0 and board[0][col] == 0:
            #upright
            i = emptySpots - 1
            j = col + 1
            while (i >= 0 and j <= 6):
                if board[i][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                i -= 1
                j += 1
            i = emptySpots - 1
            j = col + 1
            while (i >= 0 and j <= 6):
                if board[i][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                i -= 1
                j += 1
        elif col == 6 and board[0][col] == 0:
            #downleft
            i = emptySpots + 1
            j = col - 1
            while (i <= 5 and j >= 0):
                if board[i][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                i += 1
                j -= 1
            i = emptySpots + 1
            j = col - 1
            while (i <= 5 and j >= 0):
                if board[i][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                i += 1
                j -= 1
        elif board[0][col] == 0:
            #upright
            i = emptySpots - 1
            j = col + 1
            while (i >= 0 and j <= 6):
                if board[i][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                i -= 1
                j += 1
            i = emptySpots - 1
            j = col + 1
            while (i >= 0 and j <= 6):
                if board[i][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                i -= 1
                j += 1
            #downleft
            i = emptySpots + 1
            j = col - 1
            while (i <= 5 and j >= 0):
                if board[i][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                i += 1
                j -= 1
            i = emptySpots + 1
            j = col - 1
            while (i <= 5 and j >= 0):
                if board[i][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                i += 1
                j -= 1
        return self.returnValue(valCurrent, valOpp)

    def evalSecondDiagonalFunction (self, col, numCol, board):
        '''heuristic to evaluate diagonal connections'''
        valCurrent = 0
        valOpp = 0
        column = []
        for i in range(6):
            column.append(board[i][col])
        if (self.pTag in column):
            top = column.index(self.pTag)
        else:
            top = 6
        if (self.oTag in column):
            below = column.index(self.oTag)
        else:
            below = 6
        emptySpots = 5
        if top < below and top != 0:
            emptySpots = top - 1
        elif below < top and below != 0:
            emptySpots = below - 1
        if col == 0 and board[0][col] == 0:
            #downright
            i = emptySpots + 1
            j = col + 1
            while (i <= 5 and j <= 6):
                if board[i][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                i += 1
                j += 1
            i = emptySpots + 1
            j = col + 1
            while (i <= 5 and j <= 6):
                if board[i][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                i += 1
                j += 1
        elif col == 6 and board[0][col] == 0:
            #upleft
            i = emptySpots - 1
            j = col - 1
            while (i >= 0 and j >= 0):
                if board[i][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                i -= 1
                j -= 1
            i = emptySpots - 1
            j = col - 1
            while (i >= 0 and j >= 0):
                if board[i][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                i -= 1
                j -= 1
        elif board[0][col] == 0:
            #downright
            i = emptySpots + 1
            j = col + 1
            while (i <= 5 and j <= 6):
                if board[i][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                i += 1
                j += 1
            i = emptySpots + 1
            j = col + 1
            while (i <= 5 and j <= 6):
                if board[i][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                i += 1
                j += 1
            #upleft
            i = emptySpots - 1
            j = col - 1
            while (i >= 0 and j >= 0):
                if board[i][j] == self.pTag:
                    valCurrent += 1
                else:
                    break
                i -= 1
                j -= 1
            i = emptySpots - 1
            j = col - 1
            while (i >= 0 and j >= 0):
                if board[i][j] == self.oTag:
                    valOpp += 1
                else:
                    break
                i -= 1
                j -= 1
        return self.returnValue(valCurrent, valOpp)
    
    def returnValue (self, valCurrent, valOpp):
        '''evalutes the correct return value based on the heurstic functions'''
        #if the current player has to connections, win state
        if valCurrent >= 3:
            return 4
        elif valOpp >= 3 and valCurrent != 3:
            return valOpp
        elif valOpp == 2 or valCurrent == 2:
            return 2
        elif valOpp == 1 or valCurrent == 1:
            return 1
        else:
            return 0
        
    def heuristicValue (self, col, numCol, board):
        '''function to return max of the heuristic functions'''
        return max([self.evalSecondDiagonalFunction(col, numCol, board), self.evalFirstDiagonalFunction(col, numCol, board),
                    self.evalRowFunction(col, numCol, board), self.evalColFunction(col, board)])
        
    def updateQ (self, board):
        '''updates the q table'''
        #numCol = len(self.qTable)
        for i in range (0, 7):
            if (board[0][i] != 0):
                self.qTable[i] = -1
            else:
                #self.qTable[i] = self.qTable[i] + self.alpha*(1 + self.gamma * self.heuristicValue(i, self.numCol,board)- self.qTable[i])
                self.qTable[i] = self.heuristicValue(i, 6, board)
                
    def checkPlayerInsert(self, board):
        '''checks to see if the player has already inserted a coin'''
        for i in range(6):
            for j in range(7):
                if board[i][j] == self.pTag:
                    return True
        return False
    
    def choice (self, board, isEmpty):
        '''player choose optimal action'''
        if not self.checkPlayerInsert(board):
            placement = rand.randint(0,6)
            #update q table
            self.qTable[placement] = self.qTable[placement] + self.alpha*(1 + self.gamma*(1) - self.qTable[placement])
            return placement
        else:
            self.updateQ(board)
            maxValue = max(self.qTable)
            print(self.pTag, self.qTable)
            choices = []
            for i in range(7):
                if self.qTable[i] == maxValue:
                    choices.append(i)
            placement = rand.choice(choices)
            #heuristic value based off the next state
            #self.qTable[placement] = self.qTable[placement] + self.alpha*(1 + self.gamma*(self.heuristicValue(placement, self.numCol, board)) - self.qTable[placement])

            return placement                                                                              
                                                                          
