x = int(input("enter the number of levels: "))
brick = 0
level = 0
container = 0
while level <= x:
    num_brick = brick * level
    container += num_brick
    brick += 1
    level += 1
print("sum of numbers, written on bricks is: ", container)
