from numpy import *
# create arrays using numpy
arr = array([1, 2, 3, 4])
print(arr)
print(arr.dtype)
#
# [1 2 3 4]
# int64

# start with 0 and end with 16 and divide the range in 10 parts
arr2 = linspace(0, 16, 10)
print(arr2)
# [ 0.          1.77777778  3.55555556  5.33333333  7.11111111  8.88888889
#  10.66666667 12.44444444 14.22222222 16.        ]

# start with 0 and end with 10 and difference bwtween 2 numbers will be 2
arr3 = arange(0, 10, 2)
print(arr3)
# [0 2 4 6 8]

# start with 10 raise to 1 and end with 10 raise to 40, and print 5 parts in between
arr4 = logspace(1, 40, 5)
print(arr4)
# [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30
#  1.00000000e+40]

# array with 5 zeroes
arr5 = zeros(5, int)
arr6 = ones(5)

print(arr5)
print(arr6)
# [0 0 0 0 0]
# [1. 1. 1. 1. 1.]

# add value in all elements in array

arr7 = ones(5)
arr7 = arr7 + 5

print(arr7)

# array addition - arrays elements will be aadded, error if size is not same, value error
arr8 = array([1,2,3,4])
arr9 = array([1,2,3,4])
arr10 = arr8 + arr9
print(arr10)

print(min(arr8))
print(sum(arr8))
print(log(arr8))
print(len(arr8))
print(sort(arr8))
print(concatenate([arr8, arr9]))
print(id(arr8))  # address of array

arr11 = arr10.copy()
arr12 = arr10.view()

print(id(arr10))
print(id(arr11))
print(id(arr12))
print(arr11)
print(arr12)

# -- multidimensional array

arr13 = array([
    [1, 2, 3, 4, 5, 6],
    [5, 6, 7, 8, 9, 10]
    ])

print(arr13)
print(arr13.shape)
print(arr13.size)
print(arr13.ndim)

arr14 = arr13.flatten() #-- convert into one D array
print(arr14)

arr15 = arr13.reshape(3,4)
print(arr15)


m = matrix('1,2;3,4;5,6')
print(m)

