dict={'name':'DEV','Age':21,'Class':'CSBS'}
#accessing dictionary
print(dict['name'])
print(dict['Age'])
print("/////////////////")
#updting dictionary
dict['name']='Dev' #key updation
print(dict['name'])
print("/////////////////")
dict['Martial Status']='Single' #new entry
print(dict['Martial Status'])
print("/////////////////")
#deletion 
del dict['Martial Status'] #element
dict.clear() #total values in dict
del dict #total dictionary 
