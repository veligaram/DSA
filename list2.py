#sum of number digits in list
l=[12, 67, 98, 34]
res=[]
for i in l:
    sum=0
    for j in str(i):
        sum+=int(j)
    res.append(sum)
print(res)    
