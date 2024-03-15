#sort an array according to count of set bits

def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def custom_sort_key(num, index):
    return (-count_set_bits(num), index)

def sort_by_set_bits(arr):
    return sorted(arr, key=lambda x: custom_sort_key(x[0], x[1]))
array = [3, 5, 7, 15, 10, 8]
indexed_array = [(num, index) for index, num in enumerate(array)]
sorted_array = sort_by_set_bits(indexed_array)
result = [num for num, _ in sorted_array]
print(result)
