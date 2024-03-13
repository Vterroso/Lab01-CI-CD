def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

if __name__ == '__main__':
    print(addition(6, 2))
    print(subtraction(9997, 7))
    print(multiplication(645, 89))
    print(division(1, 76))