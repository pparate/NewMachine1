
class Computer:
    # -----will be called when new object is created
    # -- self is the pointer to current object in focus
    def __init__(self):
        self.name = 'pratik'
        self.age = 34

    def update(self):
        self.age = 30

    def compare(self, other):
        return self.age == other.age


# -------comp1 arg is passed automatically at first place computer(comp1,i5,16gb)
com1 = Computer()
com2 = Computer()

# -------above objects will be created in heap memory
# every object will have different addresses and have different space
# size of object ? depend on variables
#

print(com2.name)
print(com1.name)

com1.name = "Jaya"
com1.age = 35

com1.update()  # update(com1) will be passed internally and will be referred as self in method declaration in class

print(com2.name)
print(com1.name)
print(com1.age)

if com1 == com2:
    print('addresses are same')
else:
    print('addresess are not same')

if com1.compare(com2):
    print('ages are same')
else:
    print('ages are not same')