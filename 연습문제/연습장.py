import numpy as np
import random


a = np.array([[1,0],[0,1]])

print(a)

np.random.seed(10)
b =np.random.randint(1,10,size = (1,11,4))
print(b)
