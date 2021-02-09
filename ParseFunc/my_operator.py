# -*- coding: utf-8 -*-
"""
Class defining the general form of an operator
"""

#This class defines supported operators and their properties
class MyOperator:
    
    OPERATOR_PRIORITIES = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1} #Operator priorities based pn BEDMAS/PEDMAS
    FUNCTIONS = ['sin', 'cos', 'tan', 'ln', 'log', 'asin', 'acos', 'atan']
    
    def __init__(self, symbol, priority=0):
        
        self.symbol = symbol #Operator symbol, expecting type 'str'
        self.priority = priority #Operator symbol, expecting type 'int'
        
        #Assign default priority if none is given
        if self.priority == 0:
            
            self.prioritize()

    def prioritize(self):
        
        if self.symbol in  MyOperator.OPERATOR_PRIORITIES:
        
            self.priority = MyOperator.OPERATOR_PRIORITIES[self.symbol]
        
        else:
            
            self.priority = 4
        
        
    

