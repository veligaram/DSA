#bubble sort on strings

def bubblesortstrings(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = ["apple", "banana", "kiwi", "orange", "grape"]
bubblesortstrings(arr)
print("Sorted list:", arr)
