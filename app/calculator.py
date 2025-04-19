def calculate(a, b, op):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mul':
        return a * b
    elif op == 'div':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operation"
