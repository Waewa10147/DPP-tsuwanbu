num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print(f"{num1} / {num2} = Division by zero is not allowed")
print(f"{num1} * {num2} = {num1 * num2}")