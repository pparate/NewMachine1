from threading import *
from time import sleep


# main Thread

class Hi(Thread):  # Thread 1
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)


class Hello(Thread):  # Thread 2
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)


t1 = Hi()
t2 = Hello()

t1.start()  # it requires run method in class
sleep(1)
t2.start()

# -- join will wait for bove threads to complete
t1.join()
t2.join()
print('bye')
