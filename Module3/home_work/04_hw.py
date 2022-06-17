import random
n = int(input("please enter the number of elements in your list: "))
num_list = []
new_list = []
i = 0
m = 0
sum_of_positive = 0
while i < n:
    x = random.randint(-100, 100)
    num_list.insert(i, x)
    i += 1
print("here is the list of your numbers: ", num_list)
for i in num_list:
    if i > 0:
        m = i ** 0.5
        if m % 1 == 0:
            new_list.append(m)
    i += 1
print("here is the new list with square roots: ", new_list)
