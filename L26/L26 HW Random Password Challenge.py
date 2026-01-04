import random

#a functio do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#main program starts here
uppercaseletter1 =chr(random.randint(65,90)) #generate a random Uppercase letter (based on ASCII code)
uppercaseletter2 =chr(random.randint(65,90)) #generate a random Uppercase letter (based on ASCII code)
uppercaseletter3 =chr(random.randint(65,90)) #generate a random Uppercase letter (based on ASCII code)
uppercaseletter4 =chr(random.randint(65,90)) #generate a random Uppercase letter (based on ASCII code)
uppercaseletter5 =chr(random.randint(65,90)) #generate a random Uppercase letter (based on ASCII code)

#generate password using all the character, in random order
password = uppercaseletter1 + uppercaseletter2 + uppercaseletter3 + uppercaseletter4 + uppercaseletter5
password = shuffle(password)