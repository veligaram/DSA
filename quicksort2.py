#implement quick sort with randomized pivot

import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_randomized(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_randomized(arr, low, pi - 1)
        quick_sort_randomized(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
quick_sort_randomized(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
