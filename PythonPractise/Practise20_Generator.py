
def top_ten():
    num = 1
    while num <= 10:
        yield num
        num += 1

    yield 'done'


# yield keyword doesn't terminate the function, return terminates the function
# generator will give values one by one hence not all values are stored in memory at once, one by one will be stored
# generator gives us iterator
# multiple yields can be written in function

for i in top_ten():
    print(i)
