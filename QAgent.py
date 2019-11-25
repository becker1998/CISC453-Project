import numpy as np
import random as rand
from Agent import *
import Board

class QAgent(Agent):
    def __init__(self, pTag, actions, alpha, gamma, oTag):
        super(Agent,self).__init__()
        self.qTable = np.zeros(7, dtype=int)
        self.alpha = alpha        
        self.gamma = gamma
        self.pTag = pTag
        self.oTag = oTag
        self.numCol = len(self.qTable)
        
    def chooseAction (self):
        '''chooses an actions'''
        actions = board.getActions()
        actionsTemp = []
        lenActions = len(actions)
        return rand.randint(0,lenActions - 1)
    def evalColFunction (self,col, board):
        '''heuristic function that will return a value from 1-4 based on
        the danger of losing/winning in the nexr state'''
        valCurrent = 0
        valOpp = 0
        column = board[col - 1]
        #detrmines which plyers coin is sitting on top
        top = column.index(self.pTag)
        below = column.index(self.oTag)
        if top < below:
            valCurrent +=1
            #loop down column while player has a connection
            for i in range (top+1, len(column)):
                if column[i] == self.pTag:
                    valCurrent += 1
                else:
                    break
        #opponents coin is on top
        elif below < top:
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
        column = board[col - 1]
        top = column.index(self.pTag)
        below = column.index(self.oTag)
        #since we are determining row connections
        #we dont care about the filled slots
        if top < below and top != 0:
            emptySpots = top - 1
        elif below < top and below != 0:
            emptySpots = below - 1
        #3 cases when we are on the first, last or middle columns
        if col == 1:
            #if player coin is on same row
            if board[col][emptySpots] == self.pTag:
                valCurrent += 1
                #assumption we can't have a longer connection than 3 coins
                for i in range (2,4):
                    if board[i][emptySpots] == self.pTag:
                        valCurrent += 1
                    else:
                        break
            elif board[col][emptySpots] == self.oTag:
                valOpp += 1
                for i in range (2,4):
                    if board[i][emptySpots] == self.oTag:
                        valOpp += 1
                    else:
                        break
         #last column           
        elif col == numCol:
            if board[col - 1][emptySpots] == self.pTag:
                valCurrent += 1
                for i in range (col - 2,  col - 4):
                    if board[i][emptySpots] == self.pTag:
                            valCurrent += 1
                    else:
                        break
            elif board[col - 1][emptySpots] == self.oTag:
                valOpp += 1
                for i in range (col - 2, col - 4):
                    if board[i][emptySpots] == self.oTag:
                        valOpp += 1
                    else:
                        break
        else:
            if board[col][emptySpots] == self.pTag:
               valCurrent += 1
               for i in range (col + 1, col + 2):
                   if board[i][emptySpots] == self.pTag:
                        valCurrent += 1
                   else:
                       break
            elif board[col][emptySpots] == self.oTag:
                valOpp += 1
                for i in range (col + 1, col + 2):
                    if board[i][emptySpots] == self.oTag:
                         valOpp += 1
                    else:
                        break
            if board[col-2][emptySpots] == self.pTag:
               valCurrent += 1
               for i in range (col-3, col -4):
                   if board[i][emptySpots] == self.pTag:
                        valCurrent += 1
                   else:
                       break
            elif board[col-2][emptySpots] == self.oTag:
                valOpp += 1
                for i in range (col - 3, col - 4):
                    if board[i][emptySpots] == self.oTag:
                         valOpp += 1
                    else:
                        break
            
        return self.returnValue(valCurrent, valOpp)
    def evalDiagFunction (self, col, numCol, board):
        '''heuristic to evaluate diagonal connections'''
        valCurrent = 0
        valOpp = 0
        print("col Diag: ", col)
        column = board[col-1]
        
        top = column.index(self.pTag)
        below = column.index(self.oTag)
        if top < below and top != 0:
            emptySpots = top - 1
        elif below < top and below != 0:
            emptySpots = below - 1

        if col == 1:
            try:
                if board[col][emptySpots + 1] == self.pTag:
                    valCurrent += 1
                    for i in range (2,4):
                        if board[i][emptySpots + 1] == self.pTag:
                            valCurrent += 1
                        else:
                            break
                elif board[col][emptySpots + 1] == self.oTag:
                    valOpp += 1
                    for i in range (2,4):
                        if board[i][emptySpots + 1] == self.oTag:
                            valOpp += 1
                        else:
                            break
            except IndexError:
                valCurrent = valCurrent
                valOpp = valOpp
            try:
                if board[col][emptySpots - 1] == self.pTag:
                    valCurrent += 1
                    for i in range (2,4):
                        if board[i][emptySpots - 1] == self.pTag:
                            valCurrent += 1
                        else:
                            break
                elif board[col][emptySpots - 1] == self.oTag:
                    valOpp += 1
                    for i in range (2,4):
                        if board[i][emptySpots - 1] == self.oTag:
                            valOpp += 1
                        else:
                            break
            except IndexError:
                valCurrent = valCurrent
                valOpp = valOpp
        elif col == numCol:
            try:
                if board[col - 1][emptySpots + 1] == self.pTag:
                    valCurrent += 1
                    for i in range (col-2,col-4):
                        if board[i][emptySpots + 1] == self.pTag:
                            valCurrent += 1
                        else:
                            break
                elif board[col-1][emptySpots + 1] == self.oTag:
                    valOpp += 1
                    for i in range (col-2,col-4):
                        if board[i][emptySpots + 1] == self.oTag:
                            valOpp += 1
                        else:
                            break
            except IndexError:
                valCurrent = valCurrent
                valOpp = valOpp
            try:
                if board[col-1][emptySpots - 1] == self.pTag:
                    valCurrent += 1
                    for i in range (col-2,col-4):
                        if board[i][emptySpots - 1] == self.pTag:
                            valCurrent += 1
                        else:
                            break
                elif board[col-1][emptySpots - 1] == self.oTag:
                    valOpp += 1
                    for i in range (col-2,col-4):
                        if board[i][emptySpots - 1] == self.oTag:
                            valOpp += 1
                        else:
                            break
            except IndexError:
                valCurrent = valCurrent
                valOpp = valOpp
        else:
            try:
                if board[col - 1][emptySpots + 1] == self.pTag and board[col + 1][emptySpots - 1] != self.pTag:
                    valCurrent += 1
                    for i in range (col-2,col-4):
                        if board[i][emptySpots + 1] == self.pTag:
                            valCurrent += 1
                        else:
                            break
                elif board[col - 1][emptySpots + 1] == self.oTag and board[col + 1][emptySpots - 1] != self.oTag:
                    valOpp += 1
                    for i in range (col-2,col-4):
                        if board[i][emptySpots + 1] == self.oTag:
                            valOpp += 1
                        else:
                            break
                #check either side of the middle diagonals
                if board[col - 1][emptySpots + 1] == self.pTag and board[col + 1][emptySpots - 1] == self.pTag:
                    valCurrent += 2
                    #max of 2 and 1 conections 
                    if board[col - 2][emptySpots + 2] == self.pTag or board[col + 2][emptySpots - 2] == self.pTag:
                        valCurrent +=1
                if board[col + 1][emptySpots - 1] == self.pTag and board[col - 1][emptySpots + 1] == self.pTag:
                    valCurrent += 2
                    if board[col + 2][emptySpots - 2] == self.pTag or board[col - 2][emptySpots + 2] == self.pTag:
                        valCurrent +=1
                if board[col - 1][emptySpots + 1] == self.oTag and board[col + 1][emptySpots - 1] == self.oTag:
                    valOpp += 2
                    if board[col - 2][emptySpots + 2] == self.oTag or board[col + 2][emptySpots - 2] == self.oTag:
                        valOpp +=1
                if board[col + 1][emptySpots - 1] == self.oTag and board[col - 1][emptySpots + 1] == self.oTag:
                    valOpp += 2
                    if board[col + 2][emptySpots - 2] == self.oTag or board[col - 2][emptySpots + 2] == self.oTag:
                        valOpp +=1 
            except IndexError:
                valCurrent = valCurrent
                valOpp = valOpp
                            
        return self.returnValue(valCurrent, valOpp)
    
    def returnValue (self, valCurrent, valOpp):
        '''evalutes the correct return value based on the heurstic functions'''
        #if the current player has to connections, win state
        if valCurrent == 3:
            return 4
        elif valOpp == 3 and valCurrent != 3:
            return valOpp
        elif valOpp == 2 or valCurrent == 2:
            return 2
        elif valOpp == 1 or valCurrent == 1:
            return 1
        else:
            return 0
    def heuristicValue (self, col, numCol, board):
        '''function to return max of the heuristic functions'''
        return max([self.evalDiagFunction(col, numCol, board), self.evalRowFunction(col, numCol, board),
                    self.evalColFunction(col, board)])
        
    def updateQ (self, board):
        '''updates the q table'''
        #numCol = len(self.qTable)
        for i in range (0, self.numCol):
            col = board[i]
            self.qTable[i] = self.qTable[i] + self.alpha*(1 + self.gamma*
                                                          self.heuristicValue(i,self.numCol,board)- self.qTable[i]) 
    def checkPlayerInsert(self, board):
        '''checks to see if the player has already inserted a coin'''
        for i in range(6):
            for j in range(7):
                if board[i][j] == self.pTag:
                    return True
        return False
    
    def choice (self, board, isEmpty):
        '''player choose optimal action'''
        if self.checkPlayerInsert(board) == False:
            placement = rand.randint(0,6)
            #update q table
            self.qTable[placement] = self.qTable[placement] + self.alpha*(1 + self.gamma*(1) - self.qTable[placement])
            return placement
        else:
            self.updateQ(board)
            maxValue = max(self.qTable)
            placement = self.qTable.index(maxValue)
            print(placement)
            #heuristic value based off the next state
            self.qTable[placement] = self.qTable[placement] + self.alpha*(1 + self.gamma*(self.heuristicValue(placement,self.numCol,board)) - self.qTable[placement])

            return placement                                                                              
                                                                          
