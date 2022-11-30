import numpy as np
arr2 =[]
arr = np.arange(6).reshape(6//3,3)
 
for i in range(1,7):
    arr[(i-1)//3][(i-1)%3] = i
max = 0
for i in arr:
    if i[0]> max:
        max = i[0]
print(max)
