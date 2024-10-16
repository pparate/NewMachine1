class Car:
    # namespace is area where object/variables are stored
    # class variables (static) , stored in class namespace
    wheels = 4

    def __init__(self):
        # instance variables , stored in instance namespace
        self.name = 'BMW'
        self.price = 10


car1 = Car()
car2 = Car()

Car.wheels = 5

print(car2.wheels)
