# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:23:32 2019

@author: dletran
"""
#%% 0. Initilaize

import numpy as np
import pandas as pd

#%% I. List Comprehension
## A. Netsted List Comoprehension with two lists
# building 2D grid using list comprehension

rows = range(4)
cols = range(10)

arr_grid = [(x,y) for y in rows for x in cols]

np.array(np.random.random())


[(letter, number) for number in range(1,5) for letter in 'abc']

#equivalent
ls = []
for number in range(1,5):
    for letter in 'abc':
        ls.append((letter, number))

#example 2, setup
ls1 = [1, 2, 3, 4, 5]
ls2 = ['a', 'b', 'c','d', 'e']
## example 2a
[(x,y) for x in ls1 for y in ls2]
## result
[(1, 'a'),(1, 'b'),(1, 'c'),(1, 'd'),(1, 'e'),
 (2, 'a'),(2, 'b'),(2, 'c'),(2, 'd'),(2, 'e'),
 (3, 'a'),(3, 'b'),(3, 'c'),(3, 'd'),(3, 'e'),
 (4, 'a'),(4, 'b'),(4, 'c'),(4, 'd'),(4, 'e'),
 (5, 'a'),(5, 'b'),(5, 'c'),(5, 'd'),(5, 'e')]
 ## example 2b
[str(x)+y for x in ls1 for y in ls2]
## result
['1a','1b','1c','1d','1e',
'2a','2b','2c','2d','2e',
'3a','3b','3c','3d','3e',
'4a','4b','4c','4d','4e',
'5a','5b','5c','5d','5e']

## B. Dictionary
{key:value for key,value in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}

"""
What is a Zip?
* zip() takes two or more iterables
* gives you back one item from each iterabel from the same index pos
"""
#%%
total_nums = range(1, 101)

fizzbuzzes = {
        'fizz': [n for n in total_nums if n % 3 == 0],
        'buzz': [n for n in total_nums if n % 7 ==0]
}