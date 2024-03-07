#Use the following list: ['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's']. Find the index of the element 'm'.

def jump_search(arr,target):
    n=len(arr)
    step=int(n**0.5)
    prev,curr=0,0
    while curr<n and arr[curr]<target:
        prev=curr
        curr+=step
    for i in range(prev,min(curr,n)):
        if arr[i]==target:
            return i
    return -1
arr=['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's']
target='o'
print(jump_search(arr,target))
