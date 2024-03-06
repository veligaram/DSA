#K’th Smallest/Largest Element in Unsorted Array

def kthsmallest(li,k):
    li.sort()
    return li[k-1]
li=[12,3,6,7,19]
k=3
print(kthsmallest(li,k))
