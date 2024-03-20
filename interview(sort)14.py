def merge_sorted_halves(arr):
    n = len(arr)
    merged = [0] * n
    i = 0
    j = n // 2
    k = 0
    while i < n // 2 and j < n:
        if arr[i] < arr[j]:
            merged[k] = arr[i]
            i += 1
        else:
            merged[k] = arr[j]
            j += 1
        k += 1
    while i < n // 2:
        merged[k] = arr[i]
        i += 1
        k += 1
    while j < n:
        merged[k] = arr[j]
        j += 1
        k += 1

    return merged

arr = [1, 3, 5, 7, 2, 4, 6, 8]
merged_arr = merge_sorted_halves(arr)
print("Merged sorted array:", merged_arr)
