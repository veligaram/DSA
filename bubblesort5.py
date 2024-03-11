#bubble sort with range

def bubblesortrange(arr, start, end):
    for i in range(end - 1, start - 1, -1):
        for j in range(start, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubblesortrange(arr, 1, 5)
print("Sorted list in the specified range:", arr)
