
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)


print("Addition:", calculate(11, 5, add))
print("Subtraction:", calculate(11, 5, subtract))
print("Multiplication:", calculate(11, 5, multiply))
print("Division:", calculate(11, 5, divide))

print("\nTesting with another set of inputs:")
print("Addition:", calculate(48, 12, add))
print("Subtraction:", calculate(48, 12, subtract))
print("Multiplication:", calculate(48, 12, multiply))
print("Division:", calculate(48, 12, divide))