
input = input()

if input.lstrip('-').isdigit():
    number = int(input)
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
else:
    print("Invalid input. Please enter a whole number.")
