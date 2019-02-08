# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:34:40 2019

@author: longiag1
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

r_array = np.linspace(0.5,3.5,20)*1.88973
print(r_array)

### fill in this array with your actual energy values... there should be 20 values in total!!!
r_array = [0.944865, 1.24324342, 1.54162184, 1.84000026, 2.13837868, 2.43675711, 2.73513553, 3.03351395, 3.33189237, 3.63027079, 3.92864921, 4.22702763, 
           4.52540605, 4.82378447, 5.12216289, 5.42054132, 5.71891974, 6.01729816, 6.31567658, 6.614055  ]

E_array = []

# TO see the plot of the PES, uncomment the following lines
plt.plot(r_array, E_array, 'red')
plt.show()