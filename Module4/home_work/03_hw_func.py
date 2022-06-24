# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

x1 = int(input("please enter the coordinates of the first circle on the X axis: "))
y1 = int(input("please enter the coordinates of the first circle on the Y axis: "))
x2 = int(input("please enter the coordinates of the second circle on the X axis: "))
y2 = int(input("please enter the coordinates of the second circle on the Y axis: "))
r1 = int(input("please enter the radius R1 of the first circle: "))
r2 = int(input("please enter the radius R2 of the first circle: "))


def circles(x1, y1, x2, y2, r1, r2):
    lim_1x = int(x1 + r1)
    lim_11x = int(x1 - r1)
    lim_1y = int(y1 + r1)
    lim_11y = int(y1 - r1)
    lim_2x = int(x2 + r2)
    lim_22x = int(x2 - r2)
    lim_2y = int(y2 + r2)
    lim_22y = int(y2 - r2)
    if lim_11x < lim_2x < lim_1x and lim_11y < lim_2y < lim_1y and lim_11x < lim_22x < lim_1x and lim_11y < lim_22y < lim_1y:
        return ("оne circle is in the other!")
    else:
        return("the circles did not become friends")


print("result is: ", circles(x1, y1, x2, y2, r1, r2))
