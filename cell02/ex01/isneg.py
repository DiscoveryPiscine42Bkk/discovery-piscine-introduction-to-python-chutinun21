
num = input().strip()

if num.startswith('-') and num[1:].isdigit():
    number = int(num)
    print("This number is negative.")
elif num.isdigit():
    number = int(num)
    if number == 0:
        print("This number is both positive and negative.")
    else:
        print("This number is positive.")
else:
    print("This is not an integer.")
