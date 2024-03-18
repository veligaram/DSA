#bucket sort implementation

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    # Create buckets
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]
    # Put array elements in respective buckets
    for num in arr:
        index = int(num * num_buckets)
        buckets[index].append(num)
    # Sort individual buckets
    for bucket in buckets:
        insertion_sort(bucket)
    # Concatenate sorted buckets
    k = 0
    for bucket in buckets:
        for num in bucket:
            arr[k] = num
            k += 1
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
bucket_sort(arr)
print("Sorted array is:", arr)
