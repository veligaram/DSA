#sort an array of 0's ,1's and 2's

def sort_array(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr
arr = [0, 1, 2, 0, 1, 2]
sorted_arr = sort_array(arr)
print("Sorted array:", sorted_arr)
