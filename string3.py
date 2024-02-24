#to replace all characters of a list except the given charcter
li=['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
res=[]
repl_chr='$'
ret_chr='G'
for i in li:
    if i==ret_chr:
        res.append(i)
    else:
        res.append(repl_chr)
print(res)        
