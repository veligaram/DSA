#sort n numbers in range from 0 t0 n^2-1 in linear time

def sort_array(arr):
    n = len(arr)
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * n
    for num in arr:
        count[num] += 1
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    for i in range(n):
        arr[i] = output[i]
arr1 = [0, 23, 14, 12, 9]
sort_array(arr1)
print("Sorted array:", arr1)

arr2 = [7, 0, 2]
sort_array(arr2)
print("Sorted array:", arr2)

