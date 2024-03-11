#Find position of an element in a sorted array of infinite numbers

import sys

def findpos(arr,target):
    start=0
    end=1
    while target>arr[end]:
        temp=end+1
        end=end+(end-start+1)*2
        start=temp
    return binarysearch(arr,target,start,end)
def binarysearch(arr,target,start,end):
    while start<=end:
        mid=start+(end-start) //2
        if target<arr[mid]:
            end=mid-1
        elif target>arr[mid]:
            start=mid+1
        else:
            return mid
    return -1
arr=[3,5,7,9,10,90,100,130,140,160,170]
target=10
ans=findpos(arr,target)
print(ans)
