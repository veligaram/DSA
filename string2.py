#progarm to find the character position of kth word from a list of strings
li=["geekforgeeks", "is", "best", "for", "geeks"]
k=20
id=0
for word in li:
    if id+len(word)>k:
        print(str(k-id))
        break
    else:
        id+=len(word)
else:
    print("k is beyond the end of the list")
        
