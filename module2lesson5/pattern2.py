rows = int(input("Enter how many number rows you want : "))
num = 1
for i in range (rows):
    for j in range(i + 1):
        print(num, end=" " )
        num = num+1
    print()
    