#find the kth smallest

def kthsmallest(arr,k):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr[k-1]
arr=[12,3,5,7,19]
k=3
print(kthsmallest(arr,k))
    
