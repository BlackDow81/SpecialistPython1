# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######
side = int(input("Enter the side of rectangle 2<a≤30: "))
if side <= 2 or side > 30:
    print("invalid numeric value")
    input("Press Enter to exit")
else:
    x = "#" * side
    print(x)
    y= "#" + " " * (side - 2) + "#"
for a in range(0, (side - 2)):
    print(y)
print(x)
input("Press Enter to exit")
