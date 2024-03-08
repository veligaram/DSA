#count occurrences of an element

def exponentialcountoccur(arr, x):
    n = len(arr)
    if arr[0] == x:
        count = 1
        i = 1
        while i < n and arr[i] == x:
            count += 1
            i += 1
        return count
    i = 1
    while i < n and arr[i] <= x:
        i *= 2
    start, end = i // 2, min(i, n)
    return binarycountoccurrences(arr, x, start, end)

def binarycountoccurrences(arr, x, start, end):
    count = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            count += 1
            left = mid - 1
            while left >= start and arr[left] == x:
                count += 1
                left -= 1
            right = mid + 1
            while right <= end and arr[right] == x:
                count += 1
                right += 1
            return count
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    
    return 0  
arr = [1, 2, 3, 5, 8, 13, 21, 21, 34, 55, 89]
x= 21
result = exponentialcountoccur(arr, x)
print(f"Occurrences of element {x}: {result}")
