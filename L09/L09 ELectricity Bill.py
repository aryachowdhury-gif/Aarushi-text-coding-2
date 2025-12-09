# Take input of number of units consumed from the user
unit = int(input("Please enter Number of Unit you Comsumed: "))

# Check conditions of units consumed
# Then calculate amount and surcharge accordingly
# surcharge is the tax value

if(unit < 50): # Checking for units less than 50
    amount = unit *  2.60
    surcharge = 25

elif(unit < 100): # Checking for units less than 100
    amount = 130 + ((unit - 50) * 3.25)
    surcharge = 35

elif(unit < 100): # Checking for units less than 200
    amount = 130 + ((unit - 50) * 3.25)
    surcharge = 45

# Check for all the cases other than mentioned
# When units consumed are more than 200
else:
    amount = 130 + 162.50 + 520 + ((unit - 200) * 8.45)
    surcharge = 75

# Culculate and display the total electricity bill
# total amount = amount + surchange
total = amount + surcharge
print(f"Electricity Bill = {total}")