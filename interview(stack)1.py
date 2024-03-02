#postfix to prefix coversion

def post_to_pre(exp):
    stack=[]
    operators=set(['+','-','*','/'])
    for i in exp:
        if i not in operators:
            stack.append(i)
        else:
            operand2=stack.pop()
            operand1=stack.pop()
            result=i+operand1+operand2
            stack.append(result)
    return stack[0]
print(post_to_pre('AB+CD-*'))  
