#Given an array of random numbers, Push all the zero’s of a given array to the end of the array. 
from array import *
a1=array('i',[3,35,4,67,0,8,0,0,0,93,0,45,0])
ar1=[x for x in a1 if x!=0]
ar2=[x for x in a1 if x==0]
result=ar1+ar2
print(result)