#find indexex of a subarray with given sum

class Solution:
    def subArraySum(self,arr, n, target): 
        if target == 0:
            if 0 in arr:
                x = arr.index(0)
                return [x+1, x+1]
            return [-1]
        i = j = s = 0

        while i < n and j < n:
            s += arr[j]
            while s > target and i <= j:
                s -= arr[i]
                i += 1
            if s == target:
                return [i+1, j+1]
            j += 1
        return [-1]

S1= Solution()
if __name__=="__main__":
    arr=[1,2,3,7,5]
    n=5
    target=12
    print(S1.subArraySum(arr,n,target))
