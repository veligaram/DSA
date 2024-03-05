#find the first repeating element in an array of integers

def firstrepeating(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return i
    return -1
arr=[10,5,3,4,3,5,6]
print(arr[firstrepeating(arr)])
