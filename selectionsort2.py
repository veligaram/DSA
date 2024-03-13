#find maximum product of two integers

def maxprod(arr):
    n=len(arr)
    if n<2:
        return "elements must be atleast two"
    maxpr=float('-inf')
    for i in range(n-1):
        for j in range(i+1,n):
            prod=arr[i]*arr[j]
            maxpr=max(maxpr,prod)
    return maxpr
arr=[-10,-3,5,2,-7]
print(maxprod(arr))
