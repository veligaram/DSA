#find k closest elements to given value

def solution(nums,target,k,n):
    left=0
    right=n-1
    while right-left>=k:
        if abs(nums[left]-target)>abs(nums[right]-target):
            left+=1
        else:
            right-=1
    while left<=right :
        print(nums[left],end=" ")
        left+=1
nums=[12,16,22,30,35,39,42,45,48,50,53,55,56]
n=len(nums)
target=35
k=4
solution(nums,target,k,n)
