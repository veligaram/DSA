#find the minimum length unsorted subarray,sorting which makes the complete array sorted

def find_unsorted_subarray(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while start < n - 1 and arr[start] <= arr[start + 1]:
        start += 1

    if start == n - 1:
        return 0, 0
    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1
    min_val = min(arr[start:end + 1])
    max_val = max(arr[start:end + 1])
    for i in range(start):
        if arr[i] > min_val:
            start = i
            break
    for i in range(n - 1, end, -1):
        if arr[i] < max_val:
            end = i
            break

    return start, end
arr1 = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
start1, end1 = find_unsorted_subarray(arr1)
print("Indexes of the unsorted subarray:", start1, "to", end1)

arr2 = [0, 1, 15, 25, 6, 7, 30, 40, 50]
start2, end2 = find_unsorted_subarray(arr2)
print("Indexes of the unsorted subarray:", start2, "to", end2)
