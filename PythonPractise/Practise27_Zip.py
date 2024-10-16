names = ['pratik', 'parag', 'abhishek']
comps = ['jaya', 'nilu', 'punam']


zipped = zip(names, comps)
print(zipped.__next__())


zipped = list(zip(names, comps))
print(zipped)
