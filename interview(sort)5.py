#find missing elements of a range

def printMissing(arr, n, low, high):
    s = set(arr)
    for x in range(low, high + 1):
        if x not in s:
            print(x, end = ' ')
arr = [1, 3, 5, 4]
n = len(arr)
low, high = 1, 10
printMissing(arr, n, low, high)
