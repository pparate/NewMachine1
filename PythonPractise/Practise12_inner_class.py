class Student:
    def __init__(self, name, rollNo, lap):
        self.name = name
        self.rollNo = rollNo
        self.lap = lap
        self.lap2 = self.Laptop()

    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'

        def show(self):
            print(self.brand, self.cpu)


l = Student.Laptop()
s1 = Student('abc', 123, l)
s2 = Student('xyz', 456, l)

s1.show()
l1 = s1.lap
l2 = s2.lap

print(l1.brand)
print(l2.brand)

