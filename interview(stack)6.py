#evaluation of postfix expression

def evaluate_postfix(postfix_expression):
    stack = []

    operators = set(['+', '-', '*', '/'])

    for symbol in postfix_expression:
        if symbol.isdigit():
            stack.append(int(symbol))
        elif symbol in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(operand1, operand2, symbol)
            stack.append(result)
    return stack[0]

def apply_operator(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2 if operand2 != 0 else float('inf')
postfix_expression = "23*5+"
result = evaluate_postfix(postfix_expression)
print("Postfix Expression:", postfix_expression)
print("Result:", result)
