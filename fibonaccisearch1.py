#find the first occurances of an element

def fibonaccifirstoccurrence(arr, x):
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

arr = [1, 2, 3, 5, 8, 13, 21, 21, 34, 55, 89]
x = 21
result = fibonaccifirstoccurrence(arr, x)
print(f"First occurrence of element {x} found at index {result}")
