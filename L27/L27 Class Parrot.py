class Parrot:
    #class attribute / class varible
    species = "bird"

    #instance attribute or constructor
    def __init__(self, nm, h):
        self.name =nm #instance attribute / class varible
        self.age = h

#create the object of the Parrot class
blu = Parrot("Blue", 10)
woo = Parrot("Wooey", 15)

#access the class attribute
print(f"Blue is a {blu.species}")
print(f"Wooey is also a {woo.species}")

#access the instance attribute
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")