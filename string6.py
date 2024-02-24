#extract words starting with k in string list
li=["Gfg is best", "Gfg is for geeks", "I love G4G"]
k='g'
res=[]
for i in li:
    temp=i.split()
    for j in temp:
        if j[0].lower()==k.lower():
            res.append(j)
print(res)            
