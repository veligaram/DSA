#consecutive kth column difference in tuple list
t=[(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
k=1
res=[]
for i in range(len(t)-1):
    res.append(abs(t[i][k]-t[i+1][k]))
print(res)    
