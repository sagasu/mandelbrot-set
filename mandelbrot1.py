import matplotlib.pyplot as plt
import numpy as numpy

"""
 n = 0    -> 0,0,0 finite
 n = 1    -> 0,1,2,5,26 explodes
 n= -1    -> 0,-1  finite
 n= -2    -> remines finite
 n= -3    -> explodes
""" 
n = 1
z = 0

#z = z * z + n

x = numpy.arange(-3,3,1)
z = numpy.zeros_like(x)
arr = [x]
for i in range(100):
    z = z * z + n
    arr.append(numpy.abs(z) < 10)

plt.figure(figsize=(10,10))
plt.imshow(arr, extent=(x.min(), x.max(), 0, 10))
plt.colorbar()
plt.show()