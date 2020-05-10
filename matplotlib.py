# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:32:58 2020

@author: dukel
"""

#%% 00. Initialize
import matplotlib.pyplot as plt

ls_x = [1,2,3,4]
ls_y = [1,4,9,16]
ls_z = [2,3,4,5]

#%% I. Basic Plotting

plt.plot(ls_x, # x
         ls_y, # y
         color='green', 
         linestyle='dashed',
         label='dashed') #to add to legend
plt.plot([2,3,4,5], # x
         [2,3,4,5], # y
         color='#2B5B84', 
         linestyle='dashdot',
         label='dashed-dot') #to add to legend

# options to show
plt.title('TESTING123!@#') #title
plt.xlabel('lol whats up') #x axis label
plt.ylabel('Important Figures') #y axis label
plt.legend()
plt.show()


#%% II. Subplots

## FIRST PANEL
plt.subplot(2, #rows
            1, #columns
            1) #1st panel <--- THIS IS KEY
plt.plot(ls_x,
         ls_y,
         color='green',
         linestyle='dashdot')
## SECOND PANEL
plt.subplot(2, #rows
            1, #columns
            2) #1st panel <--- THIS IS KEY
plt.plot(ls_z,
         ls_z,
         color='#2B5B84',
         linestyle='dashed')
## plt.show()
plt.show()

#%% III. Setting axis limits

## FIRST PANEL
panel_1 = plt.subplot(2,1,1)
plt.plot(ls_x, ls_y, color='green', linestyle='dashdot')
panel_1.set_xlim([0,6]) # set boundaries, aka limits, to x-axis
panel_1.set_xlim([0,20])

## SECOND PANEL
panel_2 = plt.subplot(2,1,2)
plt.plot(ls_z, ls_z, color='#2B5B84', linestyle='dashed')
panel_2.set_xlim([0,6])
plt.show()
