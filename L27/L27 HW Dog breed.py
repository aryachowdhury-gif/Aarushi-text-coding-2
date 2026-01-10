class Dog:
    #class variable
    animal = 'dog'

    #the init method or constuctor
    def __init__(self, bred, color):
        #instance variable
        self.breed = bred
        self.color = color

#object of dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
Safire = Dog("Husky", "white")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('Buzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

print('Safire details:')
print('Safire is a', Safire.animal)
print('Breed: ', Safire.breed)
print('Color: ', Safire.color)