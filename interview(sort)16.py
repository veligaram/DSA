#chocolate distribution problem

def min_diff_chocolates(arr, m):
    if m == 0 or len(arr) == 0:
        return 0
    arr.sort()
    min_diff = float('inf')
    window_start = 0
    window_end = m - 1

    while window_end < len(arr):
        diff = arr[window_end] - arr[window_start]
        min_diff = min(min_diff, diff)
        window_start += 1
        window_end += 1

    return min_diff
arr1 = [7, 3, 2, 4, 9, 12, 56]
m1 = 3
print("Minimum Difference is", min_diff_chocolates(arr1, m1))

arr2 = [3, 4, 1, 9, 56, 7, 9, 12]
m2 = 5
print("Minimum Difference is", min_diff_chocolates(arr2, m2))
