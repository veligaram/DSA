# counting swaps

def bubbleswapcount(arr):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
    print("number of swaps:",count)
arr=[64,34,25,12,22,11,90]
bubbleswapcount(arr)

