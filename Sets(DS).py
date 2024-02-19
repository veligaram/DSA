Days=set(['Mon','Tue','Wed','thu','Fri','Sat','Sun'])
#accessing 
for i in Days:
    print(i)
print('/////////////') 
#Adding items
Days.add('sumday')
print(Days)
print('/////////////') 
#removing items
Days.discard('sumday') 
print(Days)
print('/////////////') 
#union
s1=set([1,3,2,4,5,7])
s2=set([4,8,9,6,2]) 
print(s1|s2)
print('/////////////') 
#intersection
print(s1&s2)
print('/////////////') 
#difference
print(s1-s2)
print('/////////////') 
#compare
subsets=s1<=s2
supersets=s2>=s1 
print(subsets)
print(supersets)
print('/////////////')  