#Next greater element for every element in given array

def NGE(arr):
    for i in range(0,len(arr),1):
        next=-1
        for j in range(i+1,len(arr),1):
            if arr[i]<arr[j]:
                next=arr[j]
                break
        print(str(arr[i])+"--"+str(next))
NGE([11,13,21,3])            
