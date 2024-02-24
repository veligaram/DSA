#ways to remove multiple empty spaces from string list
li=['gfg', ' ', ' ', 'is', '         ', 'best']
res=[i for i in li if i.strip()]
print(res)
