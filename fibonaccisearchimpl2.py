#implementation of fibonacci search using iterative method

def fibonaccisearch(arr,x):
    n=len(arr)
    if n==0:
        return -1
    fib1,fib2=0,1
    fib3=fib1+fib2
    while fib3<n:
        fib1,fib2=fib2,fib3
        fib3=fib1+fib2
    offset=-1
    while fib3>1:
        i=min(offset+fib2,n-1)
        if arr[i]<x:
            fib3=fib2
            fib2=fib1
            fib1=fib3-fib2
            offset=i
        elif arr[i]>x:
            fib3=fib1
            fib2=fib2-fib1
            fib1=fib3-fib2

        else:
            return i
    if fib2==1 and arr[offset+1]==x:
        return offset+1
    else:
        return -1
arr=[10,22,35,40,45,50,80,82,85,90,100,235]
n=len(arr)
x=235
ind=fibonaccisearch(arr,x)
if ind>=0:
    print("found at index:",ind)
else:
    print(x,"isn't present in the array");
    
