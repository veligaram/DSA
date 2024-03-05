#ceiling in a sorted array

def ceilsearch(arr,low,high,x):
    if x<=arr[low]:
        return low
    if x>arr[high]:
        return -1
    mid=(low+high)/2
    if arr[mid]==x:
        return mid
    elif arr[mid]<x:
        if mid+1<=high and x<=arr[mid+1]:
            return mid+1
        else:
            return ceilsearch(arr,mid+1,high,x)
    else:
        if mid-1>=low and x>arr[mid-1]:
            return mid
        else:
            return ceilsearch(arr,low,mid-1,x)
arr=[1,2,8,10,10,12,19]
n=len(arr)
x=20
index=ceilsearch(arr,0,n-1,x)
if index==-1:
    print("ceiling of %d doesn't exist in array"% x)
else:
    print("ceiling of %d is %d"%(x,arr[index]))
    
