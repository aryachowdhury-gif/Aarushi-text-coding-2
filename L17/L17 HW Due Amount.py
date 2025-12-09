price = 5.50 #defining price value

#define a function to calculate the different between the amount given
#and price mentioned
def calculate_change(amount_given):
    return amount_given - price

c = calculate_change(10.00) #call the function and save the return value in the variable c
print("Change the customer is due: ", c)