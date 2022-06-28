# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input("please enter a first number: "))  # Первое число
second_number = int(input("please enter a second number: "))  # Второе число
num_list = []
multiple_of_3 = 0
for number in range(first_number, second_number + 1):
    if number % 3 == 0:
        num_list.append(number)
print("here is the list of numbers multiple of 3: ", num_list)
