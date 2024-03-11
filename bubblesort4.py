#bubble sort for odd and even indices

def bubbleoddeven(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 2, 2):
            if arr[j] > arr[j + 2]:
                arr[j], arr[j + 2] = arr[j + 2], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleoddeven(arr)
print("Sorted list with odd and even indices separately:", arr)
