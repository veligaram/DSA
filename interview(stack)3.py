#convert infix expression to postfix expression

def in_to_post(exp):
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    def is_operator(symbol):
        return symbol in precedence
    def has_higher_precedence(op1,op2):
        return precedence[op1]>=precedence[op2]
    postfix=[]
    operators_stack = []

    for symbol in exp:
        if symbol.isalnum():
            postfix.append(symbol)
        elif symbol == '(':
            operators_stack.append(symbol)
        elif symbol == ')':
            while operators_stack and operators_stack[-1] != '(':
                postfix.append(operators_stack.pop())
            operators_stack.pop()  
        elif is_operator(symbol):
            while operators_stack and has_higher_precedence(operators_stack[-1], symbol):
                postfix.append(operators_stack.pop())
            operators_stack.append(symbol)

    while operators_stack:
        postfix.append(operators_stack.pop())

    return ''.join(postfix)
print(in_to_post("A + B * C + D"))
