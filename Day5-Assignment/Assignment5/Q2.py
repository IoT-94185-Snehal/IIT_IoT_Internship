import calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
print(f"{num1} - {num2} = {calculator.sub(num1, num2)}")
print(f"{num1} * {num2} = {calculator.mul(num1, num2)}")
print(f"{num1} / {num2} = {calculator.div(num1, num2)}")