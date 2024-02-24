#filter the list of string whose index in second list contains the given substring
li=["Gfg", "is", "not", "best", "and",
              "not", "for", "CS"]
li1= ["Its ok", "all ok", "wrong", "looks ok",
                        "ok", "wrong", "ok", "thats ok"]
sub_str="ok"
res=[]
for i in range(len(li1)):
    if li1[i].find(sub_str)!=-1:
        res.append(li[i])
print(res)        
