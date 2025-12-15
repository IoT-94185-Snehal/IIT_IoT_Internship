# Default Parameter Function 
def greet(name, message="Hello"):
    print(f"{message}, {name}!")


# Arithmetic Functions 
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# Function as Argument 
def operate(func, x, y):
    return func(x, y)


# Main Program 
def main():
    print("\nDEFAULT PARAMETER DEMO:")
    name = input("Enter your name: ")
    greet(name)                          
    greet(name, message="Welcome")       

    print("\nKEYWORD ARGUMENT DEMO:")
    greet(message="Good Morning", name=name)

    print("\nFUNCTION AS ARGUMENT DEMO:")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", operate(add, a, b))
    print("Multiplication:", operate(multiply, a, b))


if __name__ == "__main__":
    main()