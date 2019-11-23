from abc import abstractmethod as abstract
import random as rand
import numpy as np
import board

class Agent:
    def __init__(self, rows, cols, reward = 1):

        #each index of the table is a row of a table
        self.qTable = np.zeros(7, dtype=int)
        self.rows = rows
        self.cols = cols
        self.reward = reward
    def getRows(self):
        return board.setRows()
    def getCols(self):
        return board.setCols()
    def getReward(self):
        return self.reward

    @abstract    
    def chooseAction (self):
        '''abstract method that will chose an action'''
        pass
        
        
    @abstract
    def choice (self):
        '''abstract method that will return an agents move''
        pass
