#sort an array of non negative integers with a range of k using counting sort

def counting_sort_with_range(arr, k):
    count = [0] * (k + 1)
    output = [0] * len(arr)
    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output
arr = [4, 2, 2, 8, 3, 3, 1]
k = max(arr)
sorted_arr = counting_sort_with_range(arr, k)
print("Sorted array is:", sorted_arr)
