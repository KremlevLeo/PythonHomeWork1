# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def part (x, y):
    tmp = 0
    if x > 0 and y > 0:
        tmp = 1
        print(f"The point is in the {tmp} quarter")
    if x < 0 and y > 0:
        tmp = 2
        print(f"The point is in the {tmp} quarter")
    if x < 0 and y < 0:
        tmp = 3
        print(f"The point is in the {tmp} quarter")
    if x > 0 and y < 0:
        tmp = 4
        print(f"The point is in the {tmp} quarter")
    if x == 0 and y > 0 or y < 0:
        print("Point on X axis")
    if y == 0 and x > 0 or x < 0:
        print("Point on Y axis")

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
part(x, y)
