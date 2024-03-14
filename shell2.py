#given an array of strings sort them in lexographical order using shell sort

def shell_sort_lexicographical(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
arr = ["banana", "apple", "orange", "grape"]
shell_sort_lexicographical(arr)
print("Sorted array in lexicographical order:", arr)
