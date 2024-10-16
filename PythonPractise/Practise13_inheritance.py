class A:

    def __init__(self):
        print('in A init')

    def feature1(self):
        print('Feature 1 working')

    def feature2(self):
        print('Feature 2 working')


class B(A):
    # single level inheritance
    # (if super call is not there) if B constructor is present then it will call this constructor while creating object,
    #       else it will go for super class constructor
    # if super class constructor is present then it will show warning to call that first

    def __init__(self):
        super().__init__()
        print('in B init')

    def feature3(self):
        print('Feature 3 working')

    def feature4(self):
        print('Feature 4 working')


class C(B):
    # multilevel inheritance , C(A,B) is also possible , multiple inheritance

    def feature5(self):
        print('Feature 5 working')


#
# a1 = A()
# b1 = B()
# a1.feature1()
# a1.feature2()
# b1.feature3()
# b1.feature4()
# b1.feature1()
# b1.feature2()
#
# c1 = C()
# c1.feature1()
# c1.feature5()

b2 = B()
