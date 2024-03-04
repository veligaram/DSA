#sliding window maximum(maximum of all subarrays of size K)
def printmax(arr,N,k):
    max=0
    for i in range(N-k+1):
        max=arr[i]
        for j in range(1,k):
            if arr[i+j]>max:
                max=arr[i+j]
        print(str(max)+" ",end="")
if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    N=len(arr)
    k=3
    printmax(arr,N,k)
