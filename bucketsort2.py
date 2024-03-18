#sort an array of strings using bucket sort

def bucket_sort_strings(arr):
    num_buckets = 26 
    buckets = [[] for _ in range(num_buckets)]
    for word in arr:
        index = ord(word[0]) - ord('a')
        buckets[index].append(word)
    for bucket in buckets:
        bucket.sort()
    k = 0
    for bucket in buckets:
        for word in bucket:
            arr[k] = word
            k += 1
arr = ["apple", "banana", "grape", "kiwi", "orange"]
bucket_sort_strings(arr)
print("Sorted array is:", arr)
