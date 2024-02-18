#Rearrange array such that even positioned are greater than odd
from array import *
a1=array('i',[3,35,4,67,8,93,45])
for i in range(0,len(a1)):
    if i%2==0:
        if (a1[i] < a1[i - 1]):
                a1[i - 1], a1[i] = a1[i], a1[i - 1]
        
    else:
        if (a1[i] > a1[i - 1]):
            a1[i - 1], a1[i] = a1[i] , a1[i - 1]
print(a1)                