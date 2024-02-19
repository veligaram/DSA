#Segregate even and odd numbers using Lomuto’s Partition Scheme
def segregation(arr,n):
    j=-1
    for i in range(n):
        if arr[i]%2==0:
            j+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    return arr
print(segregation([7, 2, 9, 4, 6, 1, 3, 8, 5]),9)        