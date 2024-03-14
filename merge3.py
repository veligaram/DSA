#find kth smallest element in two sorted arrays

def merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result
def find_kth_smallest(arr1, arr2, k):
    merged = merge_sorted_arrays(arr1, arr2)
    return merged[k-1]
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
k = 3
print(f"The {k}th smallest element is:", find_kth_smallest(arr1, arr2, k))
