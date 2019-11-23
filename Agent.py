from abc import abstractmethod as abstract
import random as rand
import numpy as np

class Agent:
    def __init__(self, actions):
        qTable = np.zeros(shape=(6,7))
    

    @abstract
    def choice (self):
        '''abstract method that will return an agents move''
        pass
