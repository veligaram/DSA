#Maximum and minimum of an array using minimum number of comparisons

def minandmax(li):
    li.sort()
    return {"min":li[0],"max":li[-1]}
li=[1000,11,445,1,330,3000]
print(minandmax(li))
