import numpy as np

a = np.array([[10,20,30], [40,50,60], [70,80,90]])
b = np.array([[10,11,12], [12,13,14], [15,16,17]])

#Addition of two matrix
Addtion = a+b  
print(Addtion)

#Multiplication of two matrix
mul = np.dot(a,b)
for i in mul:
    print(i)