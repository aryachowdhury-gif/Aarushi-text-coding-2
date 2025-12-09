#Input a word or sentence
string = input("Please enter your own String: ")

reverse = ""

#loop for printing in reverse
for i in string:
    reverse = i + reverse

print()

print("The Original string = ", string)
print("The Reverse String = ", reverse)