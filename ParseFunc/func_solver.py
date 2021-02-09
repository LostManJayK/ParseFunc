# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 01:02:18 2020

This file is responsible for solving the function as defined by the user
"""
from func_parser import FuncParser
import math
import pdb

class FuncSolver:
    
    #Definition of operations for each supported operator
    OPERATIONS = {
                  '^': lambda x,y: x**y, #Exponent
                  '*': lambda x,y: x*y,  #Multiply
                  '/': lambda x,y: x/y,  #Divide
                  '+': lambda x,y: x+y,  #Add
                  '-': lambda x,y: x-y   #Subtract
                 }
    
    FUNCS = {
             'sin': lambda x: math.sin(x),
             'asin': lambda x: math.asin(x),
             'cos': lambda x: math.cos(x),
             'acos': lambda x: math.acos(x),
             'tan': lambda x: math.tan(x),
             'atan': lambda x: math.atan(x),
             'ln':  lambda x: math.log(x),
             'log': lambda x,base: math.log(x,base)
            }
    
    #This mehtod is responsible for solving the function for a given value
    ###TODO: Accept solve_val as parameter
    def solve(self, split_func, solve_val=0):
        
        print('solving...')
        
        p = FuncParser()
        
        if '(' in split_func:
            
            split_func = self.reduce_parentheses(split_func, solve_val) #Reduce parentheses
            
        op_list = p.determine_operators(split_func) #Determine operators

        #Perform calculations
        def calculate(a, op, b):
            
            return FuncSolver.OPERATIONS[op](float(a), float(b)) #Apply the appropriate function from the defined OPERATIONS and return the result
        
        
        
        #Replace all respective variales with the entered value
        ###TODO: Update to accommodate any respective variable
        subbed_func = [solve_val if i == 'x' else i for i in split_func]
        
        #Iterate through the available operators and apply them to the element on either side of them
        for op in [i.symbol for i in op_list]:
            
            cur_pos = subbed_func.index(op) #Get the position of the current operator
            
            cur_slice = subbed_func[cur_pos-1:cur_pos+2] #Get the relevant operands
            
            new_val = calculate(cur_slice[0], cur_slice[1], cur_slice[2]) #Perform operation
            
            #Insert the calculated value then truncate the  unnecessary elements
            subbed_func[cur_pos-1:cur_pos+2] = [new_val]
    
        return subbed_func[0]
    
    #Handle functions contained within brackets
    def reduce_parentheses(self, split_func, solve_val):
        
        while '(' in split_func:
            
            bracket_count = 0 #Keep track of open and closed parentheses encountered
            
            temp_func = []
            
            open_index = split_func.index('(')
            
            #Scan for the appropriate matching open and close parentheses
            for pos, element in  enumerate(split_func):
                
                if element == '(':
                    
                    bracket_count += 1
                
                elif element == ')':
                    
                    bracket_count -= 1
                    
                    if bracket_count == 0:
                        
                        close_index = pos
                        
                        break
            
            temp_func = split_func[open_index+1:close_index]
            
            split_func[open_index] = '_'

            split_func[open_index+1:close_index+1] = []
            
            reduced_value = self.solve(temp_func, solve_val)
            
            split_func = [reduced_value if x == '_' else x for x in split_func]
            
        return split_func
            
            
        
        
            