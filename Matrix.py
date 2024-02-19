from numpy import *
a1=array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
#reshape method(which we can be used to change the dimensions of the matrix)
a1.reshape(7,5)
print(a1)
print('/////////////')
#accessing
print(a1[0])
print(a1[2][1])
for i in a1:
    for x in i:
        print(x,end=" ")
    print()
print('/////////////') 
#adding a row
m=append(a1,[['Avg',12,15,13,11]],0)
print(m)
print('/////////////') 
#adding a column
m1=insert(a1,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
print(m1)
print('/////////////') 
#deleting a row
s=delete(a1,[2],0)
print(s)
print('/////////////') 
#deleting a column
s1=delete(a1,[2],1)
print(s1)
print('/////////////') 
#updating a column
a1[3]=['fri',3,4,2,5]
print(a1)
  