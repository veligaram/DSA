#counting inversions with insertion sort

def countinversions(arr):
    count=0
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            count+=1
        arr[j+1]=key
    return count
arr=[1,20,6,4,5]
print(countinversions(arr))
