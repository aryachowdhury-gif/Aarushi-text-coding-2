#add two lists using map and lambda
number1 = [1, 2, 3]
number2 = [4, 5, 6]

result = map(lambda x, y: x + y, number1, number2)

print("Addition of two lists")
print(list(result))
print()

#using map
nums = [1, 2, 3, 4, 5]

def pow(n):
    return n*n

square = list(map(pow, nums))
print("Square of numbers in list")
print(square)