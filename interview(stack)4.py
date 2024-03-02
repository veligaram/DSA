#find the nearest smaller numbers on the left side in an array

def nearest(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[i]<arr[stack[-1]]:
            ind=stack.pop()
            result[ind]=arr[i]
        stack.append(i)
    return result

print(nearest([4, 5, 2, 10, 8]))
