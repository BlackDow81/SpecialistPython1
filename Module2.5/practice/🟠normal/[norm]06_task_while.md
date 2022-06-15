x = int(input("please, enter your number: "))
sum_of_div = 0
divider = 1
while divider < x:
    if x % divider == 0:
        sum_of_div += divider
    divider += 1
print("sum of diveders is:", sum_of_div)
if sum_of_div == x:
    print("yes")
else:
    print("no")
input("Press Enter to exit")
