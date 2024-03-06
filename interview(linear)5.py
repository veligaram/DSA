#Find a Fixed Point (Value equal to index) in a given array

def find_fixed_point(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [-10, -1, 0, 3, 7, 9, 12, 17]
result = find_fixed_point(arr)

if result != -1:
    print(f"Fixed Point found at index {result}")
else:
    print("No Fixed Point in the array")
