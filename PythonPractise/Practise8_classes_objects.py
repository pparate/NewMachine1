
class Computer:
    # -----will be called when new object is created
    def __init__(self, cpu, ram):
        print('in init')
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config of computer')
        print(self.cpu, self.ram)


x = 9
a = '8'

# -------comp1 arg is passed automatically at first place computer(comp1,i5,16gb)
com1 = Computer('i5', '16gb')
com2 = Computer('i4', '8gb')

# -------above objects will be created in heap memory
# every object will have different addresses and have different space
# size of object ? depend on variables
#
print(type(com1))
print(type(a))
print(type(x))
# output
# <class '__main__.Computer'>
# <class 'str'>
# <class 'int'>

com1.config()
Computer.config(com1)


