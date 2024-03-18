#sort an array of strings attached based  on theirlength using radix

def radix_sort_strings(arr):
    max_len = max(len(s) for s in arr)
    exp = 1
    while max_len // exp > 0:
        counting_sort_strings(arr, exp)
        exp *= 10

def counting_sort_strings(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = len(arr[i]) // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = len(arr[i]) // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

arr = ["apple", "banana", "grape", "kiwi", "orange"]
radix_sort_strings(arr)
print("Sorted array is:", arr)

