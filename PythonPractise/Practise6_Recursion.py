import sys

print(sys.getrecursionlimit())


def greet():
    print('hello')
    greet()


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


print(fact(5))
