#Find a peak element which is not smaller than its neighbours

def find_max_element(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return arr[start]

arr = [5, 10, 20, 15]
max_element = find_max_element(arr)
print("Maximum Element:", max_element)

