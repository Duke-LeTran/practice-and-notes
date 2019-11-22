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