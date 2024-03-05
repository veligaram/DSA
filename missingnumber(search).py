#find the missing number

def missingnum(arr,n):
    total_sum=(n+1)*(n+2)/2
    sum_arr=sum(arr)
    return total_sum-sum_arr
arr=[1,2,3,5]
n=len(arr)
print(missingnum(arr,n))
