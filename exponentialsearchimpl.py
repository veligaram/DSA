#implementation of exponential search

def binarysearch(arr,l,r,x):
    if r>=l:
        mid=l+(r-1)//2
        if arr[mid]==x:
            return mid
        if arr[mid]>x:
            return binarysearch(arr,1,mid-1,x)
        return binarysearch(arr,mid+1,r,x)
    return -1
def exponentialsearch(arr,n,x):
    if arr[0]==x:
        return 0
    i=1
    while i<n and arr[i]<=x:
        i=i*2
    return binarysearch(arr,i//2,min(i,n-1),x)
arr=[2,3,4,10,40]
n=len(arr)
x=10
result=exponentialsearch(arr,n,x)
if result==-1:
    print("element not found")
else:
    print("element is present at index %d" %(result))
    
