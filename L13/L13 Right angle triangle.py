print("Half Pyramid Pattern of Stars (*): ")
n = int(input("enter the number of row: "))

for i in range(n): #outer loop to handle number of rows
    for j in range(i+1): #inner loop to handle number of colums
        print("* ", end = "") #display result

    print()