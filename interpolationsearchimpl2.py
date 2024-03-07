#interpolation search implementation with iteration

def interpolationsearch(arr,n,x):
    low=0
    high=(n-1)
    while low<=high and x>=arr[low] and x<=arr[high]:
        if low==high:
            if arr[low]==x:
                return low
            return -1
        pos=int(low+(((float(high-low)/(arr[high]-arr[low]))*(x-arr[low]))))
        if arr[pos]==x:
            return pos
        if arr[pos]<x:
            low=pos+1
        else:
            high=pos-1
    return -1
arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
x = 18
index = interpolationsearch(arr,n, x)
 
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
