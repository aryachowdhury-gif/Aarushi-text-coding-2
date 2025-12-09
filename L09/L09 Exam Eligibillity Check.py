#Take input for the stundent that he can attend the exam or not
medical_cause = input("did you have a medical cuase Y or N: ")

#Take input of the attendance
atten = int(input("enter the attendance of the stundent: "))

if medical_cause.upper() == 'Y': #outer IF checking the condition 1
    print("You are allowed, because you have medical condition")
else:
    if atten >= 75: #inner IF checking the condition 2
        print("Allowed. Because you don't have medical condition and your attendance is more than 75%")
    else:
        print("Not allowed. Because you don't have medical condition and your attendance is less than 75%")