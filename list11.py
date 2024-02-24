#to find all the combinations in the list with given conditions

from itertools import combinations_with_replacement

li=["GFG", [5, 4], "is",
            ["best", "good", "better", "average"]]
id=0
temp=combinations_with_replacement(li,2)
for i in list(temp):
    id=id+1
    print(id,":",i)
