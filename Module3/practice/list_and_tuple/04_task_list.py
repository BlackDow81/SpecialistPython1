# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random
n = int(input("please enter the number of elements in your list: "))
num_list = []
z = 0
sum_of_members = 0
while z < n:
    x = random.randint(-10, 10)
    num_list.insert(z, x)
    z += 1
print("here is the list of your numbers: ", num_list)
for z in num_list:
    if z >=0:
        sum_of_members += z
print("here is the sum of numbers in list: ", sum_of_members)
