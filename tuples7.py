#count tuples occurrence in list of tuples
import collections
res=collections.defaultdict(int)
l=[[('hi', 'bye')], [('Geeks', 'forGeeks')],
         [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]
for i in l:
    res[i[0]]+=1
print(res)    
