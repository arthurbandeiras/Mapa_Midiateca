import random
import numpy as np


lista = []
definitiva = []

n = 4
x1= 1651
y1= 3748
x2= 1668
y2= 3757

for _ in range(n):
    x = np.random.randint(x1,x2)
    y = np.random.randint(y1,y2)
    tmp = (x,y)
    
    while tmp in lista:
        x = np.random.randint(x1,x2)
        y = np.random.randint(y1,y2)
        tmp = (str(x),str(y))
    
    definitiva.append(tmp)

for element in definitiva:
    print(f"-20.3{element[0]}, -40.3{element[1]}")

