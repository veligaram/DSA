from array import *
a1=array('b',[10,20,30,40,50])
for x in a1:
    print(x)
#accessing 
print("/////////////////")
print(a1[3])
print(a1[2])
print("/////////////////")
#Insertion
a1.insert(1,35)
for x in a1:
    print(x)
print("/////////////////")    
#Deletion
a1.remove(10)
for x in a1:
    print(x)
print("/////////////////")    
#searching
print(a1.index(40))
print("/////////////////")    
#Updation
a1[4]=100
for x in a1:
    print(x)
            