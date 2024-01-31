def simple_calculator(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        if y != 0:  # Avoid division by zero
            return x / y
        else:
            raise ValueError("Division by zero is undefined.")


result = simple_calculator(300, 12, '-')
print(result)
