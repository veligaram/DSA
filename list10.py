#to print all possible combinations from the three digits
from itertools import permutations
res=permutations([1,2,3],3)
for i in res:
    print(i)
