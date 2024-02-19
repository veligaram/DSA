T=[[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
#accessing
print(T[0])
print(T[1][2])
for i in T: #method2 of accesing all ellements in an 2Darray
    for x in i:
        print(x,end=' ')
    print()
print('/////////////')
#updating
T[0]=[1,2,3]
T[1][2]=5
for i in T:
    for x in i:
        print(x,end=" ")
    print()
print('/////////////')    
#inserting 
T.insert(2,[4,5,6])
for i in T:
    for x in i:
        print(x,end=" ")
    print()       
print('/////////////')
#deleting
del T[3]
for i in T:
    for x in i:
        print(x,end=" ")
    print()       
print('/////////////')
