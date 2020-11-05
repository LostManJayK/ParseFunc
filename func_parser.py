# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:30:00 2020

This file is responsible for the parsing of the entered function
"""

import re
from my_operator import MyOperator

#Class defining the string parser for the function
class FuncParser:

    #This function creates a list containing operators and operands
    def split_function(self, func): #Expecting string
        
        #Define possible operators
        ops = ['\\'+op if op == '-' else op for op in MyOperator.OPERATOR_PRIORITIES] + MyOperator.FUNCTIONS
        ops = '|'.join(ops)
        pattern = r'(\w{{1,}}|[({0})])'.format(ops)
        
        print(pattern)
        
        split_func = re.findall(pattern, func.replace(' ', '')) #Separate operators and their respective operands
        
        split_func = [i for i in split_func if i != ''] #Remove empty strings        
        
        #Translate shorthand multiplication (Ex. change 2x to 2*x)
        
        ###TODO: The following will be modified to take any respective variable in the future
        
        shorthand_pattern = re.compile(r'(\w{1,})(x)') #We want to look for a number or non respective variable followed by our respective variable
                                                       #We also want to be able to separate the coefficient from the variable, so we will use groups
         
        could_be_longer = True #Track if there is still lengthening to do
        
        #While loop used to re-enumerate the list to preserve proper indexing
        while(could_be_longer): 

            print(split_func)                                 
    
            for pos, element in enumerate(split_func, start=0):
                
                try:
                
                    result = re.search(shorthand_pattern, element)
        
                    #If we find a match in the current element of the function, replace it with the updated format
                    if type(result) == re.Match:
                        
                        print('matched')
                        
                        new_elements = [result.group(1), '*', result.group(2)]
                        
                        split_func.pop(pos)
                        
                        split_func[pos:pos] = new_elements
                        
                        break
                        
                    #If we find a closing parenthesis and it is not followed by an operator or a closing bracket, add in the * operator
                    elif element == ')' and split_func[pos+1] not in MyOperator.OPERATOR_PRIORITIES and split_func[pos+1] != ')':
                        
                        split_func[pos+1:pos+1] = '*'
                        
                        break
                    
                    #If we find a opening parenthesis and it is not preceded by an operator or an opening bracket, add in the * operator
                    elif element == '(' and pos != 0  and split_func[pos-1] not in MyOperator.OPERATOR_PRIORITIES and split_func[pos-1] != '(':
                        
                            split_func[pos:pos] = '*'
                            
                            break
                    
                    #If we are now at the end and none of the conditions have been met, we are good to go
                    elif pos == len(split_func)-1:
                        
                        print('end')
                        
                        could_be_longer = False
                        
                except IndexError:
                    
                    could_be_longer = False
                
        return split_func
    
        
    #This method determines and sorts the operators being used for the given equation

    def determine_operators(self, split_func):
     
        op_list = [] #Temp list used for applying order of operations
         
        for element in split_func:
         
            if element in MyOperator.OPERATOR_PRIORITIES: #Check if the current element is recognized as an operator
                 
                op_list.append(MyOperator(element))
             
        #Sort the operators based on PEDMAS
         
        op_list.sort(key=lambda x: x.priority, reverse=True)
        
        return op_list
    

        
        
        
        
            
            
            
            
            

