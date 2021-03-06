#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:16:49 2019

@author: gurjeetkaur
"""

import numpy as np 
import time 
from matplotlib import pyplot as plt  

#Question #1 
#(Kinetic Energy of N particles)
N = 5 #(#ofparticles) 
m = np.zeros(N) #(mass)
v = np.zeros(N) #(velocity) 
for i in range(0,N): 
    m[i] = 1
    v[i] = 2.5 
print("Printing array of masses:", m)
print("Printing array of velocities:", v)     
    
T = 0.5*m*v**2 
print(T)
T_tot_loop = 0       
for i in range(0,N): 
    T_tot_loop = T_tot_loop + T[i]
    
T_tot_sum = np.sum(T) 
print("Result from loop is", T_tot_loop)
print("Result from numpy sum is", T_tot_sum)
N_array = [1, 2, 3, 4, 5]
T_array = [3.125, 6.25, 9.375,  12.5, 15.625 ]      
plt.plot( N_array, T_array, 'red')
plt.show() 

#Question #2 
N = 5
q = np.ones(N) 
x = np.linspace(0, (N-1)*0.2,N)
r = np.zeros((N,N))
for i in range(0, N): 
    for j in range(0,N):
        r[i][j] = np.sqrt( (x[i]-x[j])**2)
print("Printing array of charges", q)
print("Printing array of charges", x)
print("Printing array of charges", r)
def Potential(sep_array, charge_array):
    N = len(charge_array)
    Pot = 0
    for i in range(0,N):
        for j in range(0,N):
            if (i!=j):
                Pot = Pot + charge_array[i]*charge_array[j]/sep_array[i][j] 
    return Pot 
V_tot = Potential(r,q)
#N_array = [1, 2, 3, 4, 5]
#V_array = [0.00, 10.00, 25.00, 43.33,64.17]         
print(V_tot)


#Question #3
N_array = [1, 2, 3, 4, 5]
#T_array = [3.125, 6.25, 9.375,  12.5, 15.625 ]      
V_array = [0.00, 10.00, 25.00, 43.33, 64.17]   
start = time.time()
x = N_array
y = T_array
y1 = V_array 
plt.plot(x, y, 'red', x, y1, 'purple')

plt.show()

end = time.time()
how_long = end - start 
print("Total time to run in seconds is: ", how_long) 
