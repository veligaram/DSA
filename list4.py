#convert list to list of dictionaries
li=["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
kl=["name", "number"]
n=len(li)
res=[{kl[0]:li[i],kl[1]:li[i+1]} for i in range(0,n,2)]
print(res)
