#filter range length tuples
t=[(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
i,j=2,3
res=list(filter(lambda ele: len(ele) >=i and len(ele) <=j,t))
print(res)
