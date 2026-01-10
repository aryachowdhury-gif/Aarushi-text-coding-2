class Employee:
    #intializing constructor
    def __init__(self):
        print("Employee created")

    #calling destuctor
    def __del__(self):
        print("Destructor called")

#funtion outside of the class
def Create_obj():
    print("Making Object...")
    obj = Employee()

    print("funtion end...")
    return obj

print("Calling Create_obj() funtion...")
object_1 = Create_obj()

print("Program End...")