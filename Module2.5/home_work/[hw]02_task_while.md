a = int(input("please enter the first number: "))
b = int(input("please enter the second number: "))
if a < b:
    while a <= b:
        if a % 5 == 0:
            print(a, end="")
            a += 5
        else:
            a += 1
if a > b:
    while a >= b:
        if b % 5 == 0:
            print(b, end="")
            b += 5
        else:
            b += 1
