# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input("Enter a numer: "))
if day > 5 and day < 8:
    print(f'{day} -> Yes')
elif 1 <= day <= 5:
    print(f'{day} -> No')
else:
    print('There is no such day')    
