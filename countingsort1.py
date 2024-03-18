#sort an array of tuples based on the second using counting sort

def counting_sort_tuples(arr):
    max_val = max(arr, key=lambda x: x[1])[1]
    min_val = min(arr, key=lambda x: x[1])[1]
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [None] * len(arr)
    for _, value in arr:
        count[value - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i][1] - min_val] - 1] = arr[i]
        count[arr[i][1] - min_val] -= 1

    return output

arr = [(1, 4), (2, 3), (3, 2), (4, 1)]
sorted_arr = counting_sort_tuples(arr)
print("Sorted array is:", sorted_arr)
