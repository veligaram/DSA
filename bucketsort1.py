#sort an array of integers using bucket sort

def bucket_sort_integers(arr):
    max_val = max(arr)
    min_val = min(arr)
    num_buckets = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]
    for num in arr:
        index = num - min_val
        buckets[index].append(num)
    k = 0
    for bucket in buckets:
        for num in bucket:
            arr[k] = num
            k += 1

arr = [4, 2, 7, 1, 5, 3]
bucket_sort_integers(arr)
print("Sorted array is:", arr)
