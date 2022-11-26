# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


def dis_betw_point(Ax, Ay, Bx, By):
    res = ((Bx-Ax)**2+(By-Ay)**2)**0.5
    res = round(res, 2)
    print(f"A ({Ax},{Ay}); B({Bx},{By}) -> {res}")


Ax = int(input("Enter Ax: "))
Ay = int(input("Enter Ay: "))
Bx = int(input("Enter Bx: "))
By = int(input("Enter By: "))

dis_betw_point(Ax, Ay, Bx, By)
