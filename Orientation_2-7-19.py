#Question #1 

import numpy as np 
import time 
from matplotlib import pyplot as plt  

'''#(Kinetic Energy of N particles)
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

        
print(T1) 
plt.plot(np.linspace(0,1,N), T1, 'red')
plt.show() 

#Question #2 
Npart = 5
q = np.ones(N) 
x = np.linspace(0, (N-1)*0.2,Npart)
r = np.zeros((N,N))

for i in range(0, N): 
    for j in range(0,N):
        r[i][j] = np.sqrt( (x[i]-x[j])**2)

print("Printing array of charges", q)
print("Printing array of charges", x)
print("Printing array of charges", r)

def Potential(sep_array, charge_array,N):
    N = len(charge_array)
    Pot = 0
    for i in range(0,N):
        for j in range(0,N):
            if (i!=j):
                Pot = Pot + charge_array[i]*charge_array[j]/sep_array[i][j] 
    return Pot 
P = np.zeros(N)
for i in range(0,N):
    V = Potential(r,q,i)
    if i == 0:
        P[i] = V 
    else:
        P[i] = V + P[i-1]
        

print(V_tot)
plt.plot(np.linspace(0,1,N), P, 'blue') 
'''
#Question #3
start = time.time()
x = np.linspace(-5,6,100)
y = x**2 
plt.plot(x, y, 'red')
plt.xlim(0,6)
plt.ylim(0,36)
plt.show()

end = time.time()
how_long = end - start 
print("Total time to run in seconds is: ", how_long) 
