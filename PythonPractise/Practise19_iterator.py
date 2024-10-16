vals = [1,3,4,6]

val = iter(vals)

print(val.__next__())
print(next(val))


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1

            return value
        else:
            raise StopIteration


values = TopTen()
print(values.__next__())

for i in values:
    print(i)
