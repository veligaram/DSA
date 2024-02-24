#to check if the lsit contains three consecutive common numbers
li=[4, 5, 5, 5, 3, 8]
for i in range(len(li)-2):
    if li[i]==li[i+1] and li[i+1]==li[i+2]:
        print(li[i])
        
