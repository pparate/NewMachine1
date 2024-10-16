from functools import reduce

def add(a, b):
    return a + b


print(add(5, 4))


def add_sub(a, b):
    return a + b, a - b


res1, res2 = add_sub(5, 4)
print(res1, res2)


# - python is not pass by value or reference
# - in value we share the value, in reference we share the address of variable
#

def p(x):
    print(id(x))
    x = 8
    print(x)
    print(id(x))


a = 10
p(a)
print(id(a))


# output
# 4453252016
# 8
# 4485757808
# 4453252016

# --------- Arguments types
# default,
# positional
# variable length argument , *a will take all the arguments as tuple

def addit(a, b=4):
    print(a + b)


addit(5, 4)
addit(6)


def addit2(a, *b):
    c = a
    for i in b:
        c += i
    print(c)


addit2(1, 2, 3, 4)


# output 10

# -- keyworded variable length argument
# -- *b will take only values
# -- **b will take keyword and value
def data(a, **b):
    print(a)
    print(b)

    for i, j in b.items():
        print(i, j)


# # output
# comp globant
# age 34
# role tae

# data('pratik', 'globant', 34, 'tae')
data('pratik', comp='globant', age=34, role='tae')
# output {'comp': 'globant', 'age': 34, 'role': 'tae'}


# ----- Global variable

a = 10  # global


def something():
    a = 9  # local
    print(id(a))
    globals()['a'] = 15  #change gloabl variable, access by globals
    print(a)  # still 9
    x = globals()['a']  # address of global a and value as well
    x = 12  # x is now 12 and its local
    print(x)


something()
print(a)


def something2():
    global a
    a = 9  # its global now
    print(a)


something2()
print(a)

print('string format is like this {} {}'.format(5, 6))
# string format is like this 5 6


ff = lambda aa, b: aa + b

res = ff(5, 4)
print(res)

# --------lambda
nums = [3, 4, 5, 6, 7, 5, 8, 7]

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

doubles = list(map(lambda n: n * 2, evens))
print(doubles)

# from functools import reduce
sums = reduce(lambda n, m: n + m, doubles)
print(sums)

sums = reduce(lambda m, n: m + n, doubles)
print(sums)

