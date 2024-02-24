#select random value from list of lists
import random
li= [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
r_no=[0,1,2]
res=random.choice(li[random.choice(r_no)])
print(res)
