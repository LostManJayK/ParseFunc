# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 02:40:17 2020

@author: andre
"""

from func_parser import FuncParser
from func_solver import FuncSolver
import pdb

val = float(input("Enter the value you wish to solve for: ")) #user define 'x' value to solve for

p = FuncParser()
s = FuncSolver()

func_to_parse = input('Enter your function, without parenthesis or variables other than the respective variable "x": ')

x = p.split_function(func_to_parse)

print(s.solve(x, val))
