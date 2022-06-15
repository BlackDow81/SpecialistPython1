x = int(input("enter a number between 1 and 9 : "))
str_of_nums = ""
count = 1
while count <= x:
    str_of_nums = str(str_of_nums) + str(count)
    count += 1
    print(str_of_nums)
input("Press Enter to exit")
