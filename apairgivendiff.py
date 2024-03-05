#find a pair with the given difference

def findPair( arr, size, n):
    arr.sort();
    l = 0
    r = 1
    n = abs(n)
    while (l <= r and r < size) :
        diff = arr[r] - arr[l]
        if (diff == n and l != r): 
            print("Pair Found: (" , arr[l] , ", "
                 , arr[r] , ")")
            return True;
 
        elif (diff > n):
            l += 1
        else :
            r+=1
 
    print("No such pair")
    return False
arr = [ 1, 8, 30, 40, 100 ]
size = len(arr)
n = -60
findPair(arr, size, n)
n = 20
findPair(arr, size, n)
 
