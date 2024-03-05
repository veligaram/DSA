#implementation of linear search

def linearsearch(arr,x):
    for i in range(0,len(arr)):
        if arr[i]==x:
            return i
    return -1
if __name__=="__main__":
    arr=[2,3,4,10,40]
    x=10
    result=linearsearch(arr,x)
    if(result==-1):
        print("the guven element is not present inthe array")
    else:
        print("the element is present at index: ",result)
        
