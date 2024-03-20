#permute two arrays that sum of every pair is greater or equal to k

def is_permutation_possible(a, b, k):
    n = len(a)
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] + b[n - i - 1] < k:
            return "No"
    return "Yes"

a1 = [2, 1, 3]
b1 = [7, 8, 9]
k1 = 10
print(is_permutation_possible(a1, b1, k1))

a2 = [1, 2, 2, 1]
b2 = [3, 3, 3, 4]
k2 = 5
print(is_permutation_possible(a2, b2, k2))
