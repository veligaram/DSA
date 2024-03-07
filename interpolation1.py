#using interpolation search algorithm if there are duplicate elements , return the index of the first occurrence of the key

def interpolationduplicates(arr, key):
    low, high = 0, len(arr) - 1
    
    while low <= high and arr[low] <= key <= arr[high]:
        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == key:
            while pos > 0 and arr[pos - 1] == key:
                pos -= 1
            return pos
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1
arr=[1,2,4,6,8,10,12,14,16,16,18,20]
key=16
print(interpolationduplicates(arr,key))
