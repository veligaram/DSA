#reverse an array using stack

from collections import deque

def rev(arr,n):
    s=deque()
    for i in range(n):
        s.append(arr[i])
    x=0
    while(len(s)>0):
        top=s.pop()
        arr[x]=top
        x+=1

    for j in range(n):
        print(arr[j],end=" ")
n=4
arr=[100,200,300,400]
rev(arr,n)
        
