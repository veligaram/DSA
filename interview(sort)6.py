#sort even -placed elements in increasing and odd-placed in decreasing order

def sort_even_odd_placed(arr):
    even_placed = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    odd_placed = [arr[i] for i in range(len(arr)) if i % 2 != 0]
    even_placed.sort()
    odd_placed.sort(reverse=True)
    result = [None] * len(arr)
    for i in range(len(arr)):
        if i % 2 == 0:
            result[i] = even_placed[i // 2]
        else:
            result[i] = odd_placed[(i - 1) // 2]

    return result

arr = [7, 1, 5, 2, 4, 3, 6]
sorted_arr = sort_even_odd_placed(arr)
print("Modified array:", sorted_arr)
