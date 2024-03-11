#Find the element before which all the elements are smaller than it
#, and after which all are greater

def findElement(arr,n):
    leftmax=[None]*n
    leftmax[0]=arr[0]
    for i in range(1,n):
        leftmax[i]=max(leftmax[i-1],arr[i-1])
    rightmin=[None]*n
    rightmin[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        rightmin[i]=min(rightmin[i+1],arr[i])
    for i in range(1,n-1):
        if leftmax[i-1]<=arr[i] and arr[i]<=rightmin[i+1]:
            return i
    return -1
arr=[5,1,4,3,6,8,10,7,9]
n=len(arr)
print(findElement(arr,n))
