#implementation of stable selection sort

def stableselection(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        key = arr[mini]
        while mini> i:
            arr[mini]=arr[mini-1]
            mini-=1
        arr[i]=key
arr=[4,2,5,1,3]
stableselection(arr)
print(arr)
