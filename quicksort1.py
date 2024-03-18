#find the kthsmallest element

def kth_smallest(arr, k):
    quick_sort(arr, 0, len(arr) - 1)
    return arr[k - 1]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print("The", k, "th smallest element is:", kth_smallest(arr, k))
