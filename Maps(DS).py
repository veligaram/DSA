import collections
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}
#creation
res=collections.ChainMap(dict1,dict2)
print(res.maps,"\n")
print('/////////////') 
#accessing 
print("keys in res:{}".format(list(res.keys())))
print("values in res:{}".format(list(res.values())))
print('/////////////') 
for key,value in res.items():
    print("{}={}".format(key,value))
print()
print('/////////////')     
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))
print('/////////////') 
#map reordering
dict3 = {'day1': 'Mon', 'day2': 'Tue'}
dict4 = {'day3': 'Wed', 'day4': 'Thu'}
res1=collections.ChainMap(dict3,dict4)
print(res1.maps,'\n')
res2=collections.ChainMap(dict4,dict3)
print(res2.maps,'\n')
print('/////////////')
#updating map
dict3['day2']='Fri'
print(res1.maps)
print('/////////////')