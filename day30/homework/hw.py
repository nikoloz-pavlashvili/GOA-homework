num = int(input("enter a number "))

if num > 0:
    if num % 2 == 0:
        print("he number is positive and even")
    else:
        print("the number is positive and odd")
elif num < 0:
    print("the number is negative")
else:
    print("the number is zero")