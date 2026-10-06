user_input = input("Give me a number: ")
num = float(user_input)
if num % 1 == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")