from abc import abstractmethod as abstract
import random as rand
import numpy as np
import Board

class Agent:
    def __init__(self):

        #each index of the table is a row of a table
        self.qTable = np.zeros(7, dtype=int)

    @abstract    
    def chooseAction (self):
        '''abstract method that will chose an action'''
        pass
        
        
    @abstract
    def choice (self):
        '''abstract method that will return an agents move'''
        pass
