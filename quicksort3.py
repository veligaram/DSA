#sort an array using quick sort

def quick_sort_strings(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort_strings(less) + equal + quick_sort_strings(greater)

arr = ["apple", "banana", "grape", "kiwi", "orange"]
sorted_arr = quick_sort_strings(arr)
print("Sorted array is:", sorted_arr)
