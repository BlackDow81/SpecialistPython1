x = input("enter your number, dude: ")
stop_word = "stop"
count = 0
while x != stop_word:
    if int(x) > 0:
        count +=1
    x = input("enter your number, dude: ")
print("you entered",count, "numbers")
input("Press Enter to exit")
