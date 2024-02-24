#modulo of tupple elements
from operator import mod
t=(10, 4, 5, 6)
t1=(5, 6, 7, 5)
res=tuple(map(mod,t,t1))
print(res)
