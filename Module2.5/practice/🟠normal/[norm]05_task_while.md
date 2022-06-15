x = int(input("enter your number: "))
div_of_num = ""
divider = 2
while divider < x:
    if x % divider == 0:
        div_of_num = str(div_of_num) + str(" ") + str(divider)
    divider += 1
print("dividers of entered number: ", div_of_num)
