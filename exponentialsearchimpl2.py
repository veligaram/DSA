#implementation of exponential search in iterative method

def exponentialsearch(arr,x):
    n=len(arr)
    if n==0:
        return -1
    i=1
    while i<n and arr[i]<x:
        i*=2
    left=i//2
    right=min(i,n-1)
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            return mid
        elif arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=[2,3,4,10,40]
x=10
result=exponentialsearch(arr,x)
if result==-1:
    print("element is not found")
else:
    print("element is present at index %d"%(result))
    
