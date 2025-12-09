test_dict = {'Codingal' : 2,
              'is' : 2,
              'best' : 2,
              'for' : 2,
              'Coding' : 1
             }

#printing original dictionary
print("The original dictionay : " + str(test_dict))

#tnitialize value
v = 2

#using loop Selctive key value in dictionary
count = 0

for key in test_dict:
    if test_dict[key] == v:
        count = count + 1

#printing result
print(f"Frequency of {v} is : {count}")