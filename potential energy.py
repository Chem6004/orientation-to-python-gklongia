import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

r_array = np.linspace(0.5,3.5,20)*1.88973
print(r_array)

### fill in this array with your actual energy values... there should be 20 values in total!!!
r_array = [0.944865, 1.24324342, 1.54162184, 1.84000026, 2.13837868, 2.43675711, 2.73513553, 3.03351395, 3.33189237, 3.63027079, 3.92864921, 4.22702763, 
           4.52540605, 4.82378447, 5.12216289, 5.42054132, 5.71891974, 6.01729816, 6.31567658, 6.614055  ]

E_array = [ -107.6005848551, -111.3806002009, -112.7228746824, -113.1529129289, -113.2441488055,  -113.2151596774,  -113.1513342096, -113.0823324745,  
           -113.0170650624, -112.9596693222, -112.9104794422, -112.8689540440,  -112.8343322396, -112.8067244781, -112.7837633359, -112.7668290296 ,
           -112.7557318201, -112.7378824687,-112.737892888,-112.7397032863 ]

# TO see the plot of the PES, uncomment the following lines
plt.plot(r_array, E_array, 'red')
plt.show()
