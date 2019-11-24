import numpy as np import random as rand from Agent import * import
Board

class QAgent(Agent):
    def __init__(self, pTag, actions, alpha, gamma, oTag):
        super.__init__(actions)
        self.alpha = alpha        
        self.gamma = gamma
        self.pTag = pTag
        self.oTag = oTag
        
        
    def chooseAction (self):
        '''chooses an actions'''
        actions = board.getActions()
        actionsTemp = []
        lenActions = len(actions)
        return rand.randint(0,lenActions - 1)
    def evalColFunction (self,col, board)
        '''heuristic function that will return a value from 1-4 based on
        the danger of losing/winning in the nexr state'''
        valCurrent = 0
        valOpp = 0
        column = board[col - 1]
        top = column.index(self.pTag)
        below = column.index(self.oTag)
        if top < below:
            valCurrent +=1
            for i in range (top+1, len(column)):
                if column[i] == self.pTag:
                    valCurrent += 1
                else:
                    break
        else if below < top:
            valOpp +=1
            for i in range (below+1, len(column)):
                if column[i] == self.oTag:
                    valOpp += 1
                else:
                    break
        return returnValue(valCurrent, valOpp)
    def evalRowFunction (self, col, numCol, board):
        '''heruistic function that counts number of roww connections'''
        valCurrent = 0
        valOpp = 0
        column = board[col - 1]
        top = column.index(self.pTag)
        below = column.index(self.oTag)
        if top < below and top != 0:
            emptySpots = top - 1
        else if below < top and below != 0:
            emptySpots = below - 1
        if col == 1:
            if board[col][emptySpots] == self.pTag:
                valCurrent += 1
                for i in range (2,4):
                    if board[i][emptySpots] == self.pTag:
                        valCurrent += 1
                    else:
                        break
            else if board[col][emptySpots] == self.oTag:
                valOpp += 1
                for i in range (2,4):
                    if board[i][emptySpots] == self.oTag:
                        valOpp += 1
                    else:
                        break
                    
        else if col == numCol:
            if board[col - 1][emptySpots] == self.pTag:
                valCurrent += 1
                for i in range (col - 2,  col - 4):
                    if board[i][emptySpots] == self.pTag:
                        valCurrent += 1
                    else:
                        break
            else if board[col - 1][emptySpots] == self.oTag:
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
            else if board[col][emptySpots] == self.oTag:
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
            else if board[col-2][emptySpots] == self.oTag:
                valOpp += 1
                for i in range (col - 3, col - 4):
                    if board[i][emptySpots] == self.oTag:
                         valOpp += 1
                    else:
                        break
            
        return returnValue(valCurrent, valOpp)
    def evalDiagFunction (self, col, numCol, board):
        valCurrent = 0
        valOpp = 0
        column = board[col - 1]
        top = column.index(self.pTag)
        below = column.index(self.oTag)
        if top < below and top != 0:
            emptySpots = top - 1
        else if below < top and below != 0:
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
                else if board[col][emptySpots + 1] == self.oTag:
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
                else if board[col][emptySpots - 1] == self.oTag:
                    valOpp += 1
                    for i in range (2,4):
                        if board[i][emptySpots - 1] == self.oTag:
                            valOpp += 1
                        else:
                            break
            except IndexError:
                valCurrent = valCurrent
                valOpp = valOpp
        else if col == numCol:
            try:
                if board[col - 1][emptySpots + 1] == self.pTag:
                    valCurrent += 1
                    for i in range (col-2,col-4):
                        if board[i][emptySpots + 1] == self.pTag:
                            valCurrent += 1
                        else:
                            break
                else if board[col-1][emptySpots + 1] == self.oTag:
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
                else if board[col-1][emptySpots - 1] == self.oTag:
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
                else if board[col - 1][emptySpots + 1] == self.oTag and board[col + 1][emptySpots - 1] != self.oTag:
                    valOpp += 1
                    for i in range (col-2,col-4):
                        if board[i][emptySpots + 1] == self.oTag:
                            valOpp += 1
                        else:
                            break
                if board[col - 1][emptySpots + 1] == self.pTag and board[col + 1][emptySpots - 1] == self.pTag:
                    valCurrent += 2
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
                            
        return returnValue(valCurrent, valOpp)
    
    def returnValue (self, valCurrent, valOpp):
        if valCurrent == 3:
            return 4
        else if valOpp == 3 and valCurrent != 3:
            return valOpp
        else if valOpp == 2 or valCurrent == 2:
            return 2
        else if valOpp == 1 or valCurrent == 1:
            return 1
        else:
            return 0
    def heuristicValue (self, col, numCol, board):
        return max([evalDiagFunction(col, numCol, board), evalRowFunction(col, numCol, board),
                    evalColFunction(col, board)])
        
    def updateQ (self,board):
        numCol = len(self.qTable)
        for i in range (0, numCol):
            self.qTable[i] = self.qTable[i] + self.alpha*(self.reward + self.gamma*
                                                          heuristicValue(col,numCol,board) self.qTable[i]) 
                                                          
    def choice (self, board):
        if Board.isBoardEmpty():
            #since board is empty pick random column to drop coin
            placement = rand.randint(0,6)
            #update q table
            self.qTable[placement] = self.qTable[placement] + self.alpha*(1
                                                                          + self.gamma*(1) - self.qTable[placement]
            return placement                                                              )
        else:
            updateQ(board);
            maxValue = max(self.qTable)
            placement = self.qTable.index(maxValue)
            #heuristic value based off the next state
            maxQ = Baord.maxConnect()
            self.qTable[placement] = self.qTable[placement] + self.alpha*(1
                                                                          + self.gamma*(maxQ) - self.qTable[placement]
            return placement                                                              )
            
                                                                          
                                                                          
    
                
        
        
