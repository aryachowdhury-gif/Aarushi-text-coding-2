#Take input of a word
word = input("Please enter your own word or sentence: ")

#take input of a character
char = input("Please enter your own character: ")

i = 0
count = 0

#loop will find the occurrence of character
while(i < len(word)): #word operation
    if(word[i] == char): #check each letter of the word whether it's the same as the character we want to find
        count = count + 1

    i = i + 1 #increase the i value until reach the length of the word. i is the position of each letter in the word

#Display the result
print(f"The total number {char} character has occurred = {count} times")