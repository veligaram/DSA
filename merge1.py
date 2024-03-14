#inversion count in array using merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_count = merge_sort(arr[:mid])
    right_half, right_count = merge_sort(arr[mid:])
    merged, merge_count = merge(left_half, right_half)

    total_count = left_count + right_count + merge_count

    return merged, total_count

def merge(left, right):
    merged = []
    left_index = right_index = 0
    inv_count = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            inv_count += len(left) - left_index

    merged += left[left_index:]
    merged += right[right_index:]

    return merged, inv_count
arr = [8, 4, 2, 1]
inversion_count = merge_sort(arr)[1]
print("Inversion count:", inversion_count)
