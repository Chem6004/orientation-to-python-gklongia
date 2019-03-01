# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:39:37 2019
"""

print("Hello World!")
print("Test")

#January 18, 2019

#print("Hello World!")
import numpy as np 

#(Kinetic Energy in different ways of a single particle)
"""m = 1.0 #(mass)
v = 5.0 #(velocity)
T1 = 0.5*m*v**2 
T2 = 1/2 * m * v *v 
T3 = 0.5 * m * v* v
T4 = m*v**2/2

print(T1, T2, T3, T4) """

"""#Potential Energy - has to be done with two particles 
#have to know the position of particle 1 and 2 and the charge of particle 1 and 2. 
###Variables for particle 1
m1 = 1.0
v1 = 5.0
q1 = 1.0
x1 = 0.0

###Variables for particle 2
m2 = 1.0
v2 = 2.5
q2 = 1.0
x2 = 0.5

###Variables for pair of particles 
###r12 = the difference between the two particles 
r12 = np.sqrt((x1-x2)**2) 
V12 = q1*q2/r12 
print("separation is", r12)
print("Potential Energy is", V12) 
""" 

#for an N amount of particles 
#make m an array of numbers or a list 
#make v an array of numbers or a list
###create empty lists for each quantity 
#Npart = number of particles 
#an array of zeros 
Npart = 10
m = np.zeros(Npart)
v = np.zeros(Npart)
q = np.zeros(Npart)
x = np.zeros(Npart) 
T = np.zeros(Npart)
#print the array of zeros for m 
#print(m)


#for loop, go through the values of m v q and x as they go through different values 
#i is the variable that is being changed directly until Npart - 1 , through the for loop
Npart = 10
for i in range(0, Npart):
    m[i] = 1.0
    q[i] = 1.0
    x[i] = 0.5 * i  
    #the first particles will be at x = 0, then i will increase by 0.5 
    v[i] = 0.2* i 
    T[i] = 0.5 * m[i] * v[i]**2 

print(T)
    
print(m)
print(q)
print(x)
print(v)

#now that i have mass and velocity for the ith particle, I can calculate kinetic energy for the ith particle (T)






