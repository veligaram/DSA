#find the strongest neighbour
li=[1,2,2,3,4,5]
res=[]
for i in range(len(li)-1):
    x=max(li[i],li[i+1])
    res.append(x)
for j in res:
    print(j,end=" ")
