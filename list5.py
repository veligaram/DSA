#convert lists of list to dictionary
li=[['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
res={tuple(sub[:2]): tuple(sub[2:]) for sub in li}
print(res)
