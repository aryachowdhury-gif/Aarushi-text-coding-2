class Ferrari:
    def fuel_type(self):
        print("Petrol")
    
    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")
    
    def max_speed(self):
        print("Max speed 240")

ferrari = Ferrari()
bmw = BMW()

#literate object of same type
for car in (ferrari, bmw):
    #call method without checking class of object
    car.fuel_type()
    car.max_speed()