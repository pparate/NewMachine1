class Student:

    def __init__(self):
        pass

    def sum(self):
        print('sum1')

    #
    # def sum(self, other):
    #     print('sum2')

    # method overloading is not supported in python, it will take it as re declaration

    def showName(self):
        print('Student')


class Pratik(Student):
    def __init__(self):
        super().__init__()

    def showName(self):
        print('pratik')

    def check(self):
        pass


s1 = Student()
print(s1.sum()) # sum doesn't return anything so it will return None'
s2 = Pratik()
print(s2.showName())
