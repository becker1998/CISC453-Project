from abc import abstractmethod as abstract
import random as rand
import numpy as np

class Agent:
    def __init__(self):

    @abstract
    def choice (self):
        '''abstract method that will return an agents move''
        pass
