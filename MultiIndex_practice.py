# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:56:44 2019

https://pandas.pydata.org/pandas-docs/stable/reference/indexing.html#multiindex
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.set_levels.html#pandas.MultiIndex.set_levels

@author: dletran
"""
import pandas as pd
import numpy as np

idx = pd.MultiIndex.from_tuples([(1, u'one'), (1, u'two'),
                                 (2, u'three'), (2, u'four')], 
                                 names=['foo', 'bar']) #lvl0 is foo; lvl1 is bar

df = pd.DataFrame(columns=idx, 
                  data=np.array([[1, 2, 3, 5], 
                                 [4, 5, 6, 5], 
                                 [7, 8, 9, 5], 
                                 ['a','b','c', 'd']]))

df2 = df.copy()

df2.columns = df.columns.set_levels([3,4], level=0)

df2