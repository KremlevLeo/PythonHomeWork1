def Part(x, y):
    tmp = 0
    if x > 0 and y > 0:
        tmp = 1
    if x < 0 and y > 0:
        tmp = 2
    if x < 0 and y < 0:
        tmp = 3
    if x > 0 and y < 0:
        tmp = 4
    print(f"The point is in the {tmp} quarter")

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
Part(x,y)
