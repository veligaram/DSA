#sort the array in descending order using the shell sort algorithm

def shellsortdesc(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] < temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
arr = [12, 34, 54, 2, 3]
shellsortdesc(arr)
print("Sorted array in descending order:", arr)
