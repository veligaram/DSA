tup1=('physics','chemistry',1997,2000)
#accessing 
print(tup1[0])
print(tup1[-1])
print("/////////////////")
#updating tuple(we cannot update tuple but we can create new one by concantenation)
t1=(1,2)
t2=('x','y')
t3=t1+t2
print(t3)
print("/////////////////")
#deleting tuple (we cannot delete individual element in tuple but we can delete entire tuple)
print(t2)
del t2
print("after delete operaation:")
#print(t2)