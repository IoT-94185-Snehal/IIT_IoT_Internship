num1 = float(input("Enter the first number (dividend): "))
num2 = float(input("Enter the second number (divisor): "))

if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print(f"Result of division is={result}")