import arithmetic
import string_ops

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"{num1} + {num2} = {arithmetic.add(num1, num2)}")
print(f"{num1} * {num2} = {arithmetic.multiply(num1, num2)}")


s=input("Enter the string:")
print("Reversed string:", string_ops.reverse_string(s))
print("Vowel count:", string_ops.count_vowels(s))