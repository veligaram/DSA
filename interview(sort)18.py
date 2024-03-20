#Minimum swaps to make two arrays consisting unique elements identical\

def min_swaps_to_match(arrA, arrB):
    n = len(arrA)
    index_map = {val: i for i, val in enumerate(arrB)}
    visited = [False] * n
    swaps = 0

    for i in range(n):
        if not visited[i]:
            j = i
            cycle_size = 0
            while not visited[j]:
                visited[j] = True
                j = index_map[arrA[j]]
                cycle_size += 1
            swaps += cycle_size - 1

    return swaps
arrA = [3, 6, 4, 8]
arrB = [4, 6, 8, 3]
print("Minimum number of swaps:", min_swaps_to_match(arrA, arrB))
