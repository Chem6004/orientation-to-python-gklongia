# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:40:58 2019

@author: longiag
"""

import numpy as np
import pylab
import math
from matplotlib import pyplot as plt
pi = math.pi
m = 1.0
l = 10.0
    
def H_ij(i, j):
   # i = i+1
   # j = j+1
    if i==j:
        ham_int = (2) * np.sin(j * np.pi) * np.sin(i* np.pi)  + (np.pi**2 * j**2) / 2
    else:
        ham_int =  (2) * np.sin(j * np.pi) * np.sin(i* np.pi)
        

    return ham_int

H_mat = np.zeros((3,3))
for i in range(1,4):
    for j in range(1,4):
        H_mat[i-1][j-1] = H_ij(i, j)
print(H_mat)

c = np.zeros(3)
c[0] = 1
c[1] = 0
c[2] = 0

Hc = np.dot(H_mat,c)
E = np.dot(np.transpose(c),Hc)
print (E)
print ("Ground state energy is", E )

E_opt, c_opt = np.linalg.eig(H_mat) 
print(E_opt[0]) 
print(c_opt[0]) 