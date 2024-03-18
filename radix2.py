#sort an array of integers with negetive numbers using radix sort

def radix_sort_with_negatives(arr):
    positive_nums = [x for x in arr if x >= 0]
    negative_nums = [-x for x in arr if x < 0]

    radix_sort(positive_nums)
    radix_sort(negative_nums)

    return negative_nums[::-1] + positive_nums

arr = [170, -45, 75, -90, 802, -24, 2, -66]
sorted_arr = radix_sort_with_negatives(arr)
print("Sorted array with negative numbers is:", sorted_arr)
