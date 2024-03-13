#implementation of selection sort

import sys

def selectionsort(arr):
    for i in range(len(arr)):
        mini=i
        for j in range(i+1,len(arr)):
            if arr[mini]>arr[j]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
arr=[64,25,12,22,11]
selectionsort(arr)
for i in range(len(arr)):
    print("%d" %arr[i],end=" ")
