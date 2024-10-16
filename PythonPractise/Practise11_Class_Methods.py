class Stud:
    school = 'bdm'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance method because of (self)
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # accessors
    def getM1(self):
        return self.m1

    # mutator
    def setM1(self, val):
        self.m1 = val

# class method, can be accessible by reference variable as well and class name
    # can access on cls variables ( class state)
    @classmethod
    def getSchool(cls):
        return cls.school

# static method, can be accessible by reference variable as well and class name
# cannot access cls or self variables (class and object state)
    @staticmethod
    def info():
        print('this is stud class')


s1 = Stud(34, 45, 56)
print(s1.avg())
print(Stud.getSchool())
Stud.info()
print(s1.getSchool())
s1.info()
