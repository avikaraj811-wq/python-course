rows = int(input("Enter the number of rows : "))
if rows % 2 == 0:
    halfD = int(rows / 2)
else:
    halfD = int(rows / 2 + 1)
space = halfD - 1
for i in range(1, halfD + 1):
    for j in range(1, space + 1):
        print(end = " ")
    space = space - 1
    num = 1
    for j in range(2 * i -1):
        print(end = str(num))
        num = num+1
    print()
space = 1
for i in range(1, halfD ):
    for j in range(1, space + 1):
        print(end = " ")
    space = space+1
    num = 1
    for j in range(1, 2* (halfD - i)):
        print(end = str(num))
        num = num +1
    print( )