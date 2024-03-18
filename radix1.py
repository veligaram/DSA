#sort in array of integers in decending order \\

def radix_sort_descending(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_descending(arr, exp)
        exp *= 10

def counting_sort_descending(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(8, -1, -1):
        count[i] += count[i + 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort_descending(arr)
print("Sorted array in descending order is:", arr)
