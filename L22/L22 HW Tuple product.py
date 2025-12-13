def mutiple_tuple(num):
    temp = list(num)
    product = 1

    for x in temp:
        product = product * x

    return product

num = (4, 3, 2, 2, -1, 18)
print("Original Tuple: ")
print(num)
print()

result = mutiple_tuple(num)

print("Product - multiplying all the numbers of the said tule:",result)
print()