# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:00:40 2019

@author: dletran
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

# x range
x = np.linspace(-3.0, 3, num=100)

# y, equation
y = np.abs(np.sin(x)) + 5 * np.exp(-x **100) * np.cos(x)

plt.plot(x,y)
