# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Формат входных данных
# Вводятся 3 натуральных числа n, m и k. Точно известно, что  k ≠ n * m.
# Формат выходных данных
# Выведите «YES», если можно отломить от шоколадки ровно k долек, и «NO» иначе.

n = int(input("Enter the length of the chocolate bar n:"))
m = int(input("Enter the width of the chocolate bar m:"))
k = int(input("Enter the number of pieces you want k:"))

if n == k or m == k:
    print("Yes")
if n != k and m != k:
    print("No")
input('Press Enter to exit')
