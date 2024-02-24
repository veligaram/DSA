#flatten tuple of list to tuple
t=([5, 6], [6, 7, 8, 9], [3])
res=tuple(sum(t,[]))
print(res)
