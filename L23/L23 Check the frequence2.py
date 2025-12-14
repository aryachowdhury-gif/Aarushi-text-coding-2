name = {'My' : 1,
        'is' : 1,
        'Aarushi' : 3,
       }
print("The original dictionay : " + str(name))
v = 1
count = 0

for key in name:
    if name[key] == v:
        count = count + 1

#printing result
print(f"Frequency of {v} is : {count}")