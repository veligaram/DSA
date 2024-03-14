#sort elements by frequancy

def frequency_sort(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    sorted_arr = sorted(arr, key=lambda x: (-frequency[x], arr.index(x)))
    
    return sorted_arr
arr1 = [2, 5, 2, 8, 5, 6, 8, 8]
arr2 = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
print("Output:", frequency_sort(arr1))
print("Output:", frequency_sort(arr2))
