cost = float(input("Please enter the price of item:"))
n = int(input("Please enter goods quantity: "))
# price_of_items = x
x = 1
while x <= n:
    price_of_items = x * cost
    print("price of", x, "items", "{:,.2f}".format(price_of_items), "rub")
    x += 1
input("Press Enter to exit")
