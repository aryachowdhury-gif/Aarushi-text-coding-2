num = int(input("You want odd and even numbers under what value? : "))

odd_list = [i for i in range(num) if i%2!=0]
print("List of odd number:", odd_list)
print()

even_list = [i for i in range(num) if i%2!=0]
print("List of even number:", even_list)
print()

fruit = ['apple', 'banana', 'mango', 'papaya', 'grape']
Fruit = [x[0].upper()+x[1:] for x in fruit]
print(("Fruit as proper noun : ",Fruit))