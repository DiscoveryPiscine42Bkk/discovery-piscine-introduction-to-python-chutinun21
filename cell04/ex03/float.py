num = input("Give me a number: ")

try:
    num = float(num)
    if num == int(num):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("That's not a valid number.")