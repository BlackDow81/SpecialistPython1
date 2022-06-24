def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    sum1 = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    sum2 = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
    if sum1 == sum2:
        print("your ticket is lucky! :)")
    else:
        print("your ticket is not lucky :(")


ticket_number = input("please enter six numbers: ")
print(lucky_ticket(ticket_number))

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
