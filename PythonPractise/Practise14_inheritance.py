class A:

    def __init__(self):
        print('in A init')

    def feature1(self):
        print('Feature 1 of A working')

    def feature2(self):
        print('Feature 2 working')


class B:

    def __init__(self):
        super().__init__()
        print('in B init')

    def feature1(self):
        print('Feature 1 of B working')

    def feature4(self):
        print('Feature 4 working')


class C(A, B):
    # multiple inheritance

    def __init__(self):
        super().__init__()  # this will call A init ( left to right inheritance params)
        print('in C init')

    def feature5(self):
        print('Feature 5 working')
        super().feature1()


c1 = C()
c1.feature1()  # this will call A method , MRO method resultion order left to right C(A,B)
