# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:32:58 2020

@author: dukel
"""


import matplotlib.pyplot as plt

plt.plot([1,2,3,4], # x
         [1,4,9,16], # y
         color='green', linestyle='dashed') #line
plt.plot([2,3,4,5], # x
         [2,3,4,5], # y
         color='#2B5B84', linestyle='dashdot')
plt.ylabel('Important Figures') #y axis label
plt.xlabel('lol whats up') #x axis label
plt.title('TESTING123!@#') #title
plt.show()