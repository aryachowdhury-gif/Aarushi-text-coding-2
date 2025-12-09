r = int(input("Enter the Total number of row: "))

print("Mirrored right triangle star pattern")
for i in range(1,r+1):
    for j in range(1,r+1):
        if(j <= r -i):
            print(' ',end= '  ')
        else:
            print('*', end= '  ')
    print()