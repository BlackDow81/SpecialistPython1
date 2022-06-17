import random
n = int(input("please enter the number of elements in your list: "))
num_list = []
i = 0
while i < n:
    x = random.randint(-100, 100)
    num_list.insert(i, x)
    i += 1
print(num_list)
