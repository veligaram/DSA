#implementation of fibonaccisearch
from bisect import bisect_left

def fibonaccisearch(arr,x,n):
    fib2=0
    fib1=1
    fib=fib2+fib1
    while(fib<n):
        fib2=fib1
        fib1=fib
        fib=fib2+fib1
    offset=-1
    while (fib>1):
        i=min(offset+fib2,n-1)
        if arr[i]<x:
            fib=fib1
            fib1=fib2
            fib2=fib=fib1
            offset=i
        elif(arr[i]>x):
            fib=fib2
            fib1=fib1-fib2
            fib2=fib-fib1
        else:
            return i
    if (fib1 and arr[n-1]==x):
        return n-1
    return -1
arr=[10,22,35,40,45,50,80,82,85,90,100,235]
n=len(arr)
x=235
ind=fibonaccisearch(arr,x,n)
if ind>=0:
    print("found at index:",ind)
else:
    print(x,"isn't present in the array")
