# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:34:49 2021

@author: mabre
"""


from random import randint

def roll(sides,n=1,mod=0):
    total = 0
    for i in range(n):
        total += randint(1,sides)
    return total + mod