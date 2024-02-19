#Given a sorted array of positive integers, rearrange the array alternately 
def rearrange(a1,n):
    temp=n*[None]
    smallest,largest=0,n-1
    flag=True
    for i in range(n):
        if flag is True:
            temp[i]=a1[largest]
            largest-=1
        else:
            temp[i]=a1[smallest]
            smallest+=1
        flag=bool(1-flag) 
    for i in range(n):
        a1[i]=temp[i]
    return a1
print(rearrange([1, 2, 3, 4, 5, 6],6) )                