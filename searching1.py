#Given Array of size n and a number k, find all elements that appear more than n/k times

def solution(arr,n,k):
    x=n//k
    freq={}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]]+=1
        else:
            freq[arr[i]]=1
    for i in freq:
        if (freq[i]>x):
            print(i)
arr=[1,1,2,2,3,5,4,2,2,3,1,1,1]
n=len(arr)
k=4
solution(arr,n,k)
