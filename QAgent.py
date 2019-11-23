import numpy as np
import random as rand
from Agent import *
import Board

class QAgent(Agent):
    def __init__(self,actions, alpha, gamma):
        super.__init__(actions)
        self.alpha = alpha        
        self.gamma = gamma
        
    def chooseAction (self):
        '''chooses an actions'''
        actions = board.getActions()
        actionsTemp = []
        lenActions = len(actions)
        return rand.randint(0,lenActions - 1)
    def chooseState (self):

    def choice (self):
        R = Board.getRewards
        if Board.isBoardEmpty():
            R = 1
            #since board is empty pick random column to drop coin
            placement = rand.randint(0,6)
            #update q table
            self.qTable[placement] = self.qTable[placement] + self.alpha*(1
                                                                          + self.gamma*(1) - self.qTable[placement]
            return placement                                                              )
        else:
            maxValue = max(self.qTable)
            placement = self.qTable.index(maxValue)
            #heuristic value based off the next state
            maxQ = Baord.maxConnect
            self.qTable[placement] = self.qTable[placement] + self.alpha*(1
                                                                          + self.gamma*(maxQ) - self.qTable[placement]
            return placement                                                              )
            
                                                                          
                                                                          
    
                
        
        
