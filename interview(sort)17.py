#Bucket sort to sort an array with negative numbers

def bucket_sort_float(arr):
    min_val = min(arr)
    max_val = max(arr)
    num_buckets = len(arr)
    range_val = max_val - min_val
    buckets = [[] for _ in range(num_buckets)]
    for num in arr:
        index = int((num - min_val) / (range_val / num_buckets))
        if index == num_buckets:
            index -= 1
        buckets[index].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr
arr = [-0.897, 0.565, 0.656, -0.1234, 0, 0.3434 ]
sorted_arr = bucket_sort_float(arr)
print("Sorted array:", sorted_arr)
