#reverse individual word

def rev(s):
    word=''
    res=s.split()
    for i in res:
        word=i[::-1]
        print(word,end=" ")
if __name__=='__main__':
    s="Hello World"
    rev(s)
