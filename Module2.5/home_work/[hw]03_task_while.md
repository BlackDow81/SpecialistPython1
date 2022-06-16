n = int(input("please enter the number between 1 and 9: "))
x = 1
y = 1
while x <= n:
    while y <= n:
        print(x*y, end="\t")
        y +=1
    print("\n")
    y = 1
    x += 1
