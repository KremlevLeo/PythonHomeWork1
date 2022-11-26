# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def result_quat (quater):
    if quater == 1:
        print("X>0 ; Y>0")
    if quater == 2:
        print("X<0 ; Y>0")
    if quater == 3:
        print("X<0 ; Y<0")
    if quater == 4:
        print("X>0 ; Y<0")

quater = int(input("Enter number of quater: "))
result_quat(quater)
