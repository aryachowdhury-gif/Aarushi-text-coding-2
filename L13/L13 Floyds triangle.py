rows = int(input("Please enter the total number of rows: "))
number = 1 #intialise by 1

print("Floyd's Tiriangle")

for i in range(1, rows + 1): #representind rows
    for j in range(1, i + 1): #representing columns
        print(number, end ='  ')
        number = number + 1
    
    print()