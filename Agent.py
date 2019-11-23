from abc import abstractmethod as abstract
import random as rand
import numpy as np
import board

class Agent:
    def __init__(self, rows, cols):

        #each index of the table is a row of a table
        self.qTable = np.zeros(shape=(6,7))
        self.rows = rows
        self.cols = cols
        
    def getRows(self):
        return board.setRows()
    def getCols(self):
        return board.setCols()
    @abstract    
    def chooseAction (self):
        '''abstract method that will chose an action'''
        pass
        
        
    @abstract
    def choice (self):
        '''abstract method that will return an agents move''
        pass
