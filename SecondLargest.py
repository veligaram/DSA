from array import *
a1=array('i',[3,35,4,67,8,93,45])
temp=0
for i in range(0,len(a1)):
    for j in range(i+1,len(a1)):
        if (a1[i]<a1[j]):
            temp=a1[i]
            a1[i]=a1[j]
            a1[j]=temp
print(a1[1])            