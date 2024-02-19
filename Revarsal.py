#Given an array arr[] of size N, the task is to rotate the array by d position to the left.
def reversal(arr,n):
    result=arr[n:len(arr)]+arr[0:n]
    return result
print(reversal([1, 2, 3, 4, 5, 6, 7],2))