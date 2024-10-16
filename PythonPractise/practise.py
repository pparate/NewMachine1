import math

from array import *

# -----------------Math FUnctions
# x = math.sqrt(25)
# print(x)
#
# print(math.floor(2.9))
# print(math.ceil(3.2))
# print(math.pow(3, 2))
#
# # ---------------user input
# x = int(input('enter a number'))
# y = int(input('enter 2nd number'))
# print(x + y)
#
# x = eval(input('enter expression'))
# print(x)

# -----------Command line input
# import sys
# sys.argv[0]-- is a filename
# a = int(sys.argv[1])
# b = int(sys.argv[2])

# will stay on same line after printing
print('abc', end='')
# goto next line after printing
print('abc')
print('xyz')

# ------------- For Loop
xy = 'pratik'
for i in xy:
    print(i, end='')

for i in ['a', 'b', 'b']:
    print(i)

for i in range(1, 10, 1):
    print(i)

for i in range(1, 100):
    if i % 2 != 0:
        pass
    elif i % 3 == 0:
        continue
    else:
        break

# ---------- While Loop
while i in range(1, 10):
    i += 1
    print(i)

# -----------Nested For Loop
for i in range(1, 5):
    for j in range(1, 5):
        print('# ', end='')
    print()

for i in range(1, 5):
    for i in range(4 - i):
        print('# ', end='')
    print()

# ------------ For Else  -- else will work when break is there in for loop and for loop never got broke
for num in [11, 16, 21, 22]:
    if num % 5 == 0:
        print(num)
        break
else:
    print('nothing printed')

# -------- Arrays
# i -- integer
# f -- float
# d -- double
# u -- char
vals = array('i', [1, 2, 3, 4])
print(vals)

vals.reverse()
print(vals)

vals2 = array(vals.typecode, (a for a in vals))
print(vals2)

for i in vals:
    print(i, end='')

print(vals.index(1))


