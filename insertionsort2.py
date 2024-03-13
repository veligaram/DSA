#find the intersection of two sorted arrays

def intersection(arr1,arr2):
    result=[]
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] <arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            result.append(arr1[i])
            i+=1
            j+=1
    return result
arr1=[1,2,4,5,7]
arr2=[2,3,5,6]
print(intersection(arr1,arr2))
