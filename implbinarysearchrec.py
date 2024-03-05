#implementation of recursive binary search

def binarysearchrec(arr,x,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearchrec(arr,x,low,mid-1)
        else:
            return binarysearchrec(arr,x,mid+1,high)
    else:
        return -1
if __name__=="__main__":
    arr=[ 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x=5
    print(binarysearchrec(arr,x,0,len(arr)-1))
    
