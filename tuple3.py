#multiply adjacent elements
t=(1, 5, 7, 8, 10)
res=tuple(i*j for i,j in zip(t,t[1:]))
print(res)
