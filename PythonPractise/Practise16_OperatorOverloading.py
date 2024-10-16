a = 5
b = 6

print(a + b)
# behind the scenes below
print(int.__add__(a, b))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s = Student(m1, m2)
        return s

    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        if m1 < m2:
            return False
        else:
            return True

    # will print values now instead of object address.
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

    def sum(self):
        print('sum1')

    def sum(self, other):
        print('sum2')


s1 = Student(55, 100)
s2 = Student(65, 110)

s3 = s1 + s2  # Student.__add__(s1,s2) , behind the scenes
print(s3.m1)
print(s3.m2)

if s1 < s2:
    print('s2 wins')
else:
    print('s1 wins')

# is __str__ is overridden then it will print from overiddden method, else object address will be printed
print(s1)

