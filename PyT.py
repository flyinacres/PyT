import itertools

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print list(races)
