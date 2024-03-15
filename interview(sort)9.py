#sort a nearly sorted(or K sorted ) array

def nearlysort(arr,n,k):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=max(0,i-k) and arr[j]>key:
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=key
    for i in range(n):
        print(arr[i],end=" ")
    print()
arr=[2,6,3,12,56,8]
n=6
k=3
nearlysort(arr,n,k)
