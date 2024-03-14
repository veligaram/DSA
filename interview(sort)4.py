#sort strings using bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = ["banana", "apple", "orange", "grape", "pineapple"]
bubble_sort(arr)
print("Sorted array:", arr)
